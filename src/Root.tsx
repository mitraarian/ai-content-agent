import React, {useEffect, useLayoutEffect, useState} from "react";
import {AbsoluteFill, Audio, cancelRender, Composition, continueRender, delayRender, interpolate, Sequence, spring, staticFile, useCurrentFrame, useVideoConfig} from "remotion";

type Theme = Record<"bg"|"panel"|"line"|"white"|"muted"|"cyan"|"amber", string>;
type Scene = {title:string; summary:string; left:string; right:string; note:string; startFrame:number; durationInFrames:number; audio:string};
type Cue = {fromFrame:number; toFrame:number; text:string};
type Video = {title:string; exampleLabel:string; footer:string; width:number; height:number; fps:number; durationInFrames:number; theme:Theme; scenes:Scene[]; captions:Cue[]};
type Props = {video: Video};
const clamp = {extrapolateLeft:"clamp",extrapolateRight:"clamp"} as const;

// Extracted motion primitive: frame-driven spring reveal, independent of content.
const Reveal: React.FC<{children:React.ReactNode;delay:number}> = ({children,delay}) => {
  const frame=useCurrentFrame();const {fps}=useVideoConfig();
  const value=spring({frame:frame-delay,fps,config:{damping:22,stiffness:110}});
  return <div style={{opacity:interpolate(frame,[delay,delay+16],[0,1],clamp),transform:`translateY(${(1-value)*34}px)`}}>{children}</div>;
};
const Panel:React.FC<{children:React.ReactNode;color:string;theme:Theme}> = ({children,color,theme}) =>
  <div style={{padding:34,border:`2px solid ${color}`,borderRadius:16,background:theme.panel}}>{children}</div>;

const MotionScene:React.FC<{scene:Scene;index:number;video:Video}> = ({scene,index,video}) => {
  const frame=useCurrentFrame();const c=video.theme;
  return <AbsoluteFill style={{padding:"190px 76px 450px"}}>
    <div data-copy style={{fontSize:30,color:c.amber,letterSpacing:1}}>{String(index+1).padStart(2,"0")} / {video.exampleLabel}</div>
    <h1 data-copy style={{fontSize:76,lineHeight:1.12,letterSpacing:-2,margin:"42px 0 28px",fontWeight:700}}>{scene.title}</h1>
    <p data-copy style={{fontSize:48,lineHeight:1.3,color:c.muted,margin:"0 0 55px"}}>{scene.summary}</p>
    <Reveal delay={5}><Panel color={c.cyan} theme={c}>
      <div style={{fontSize:30,color:c.cyan,marginBottom:15}}>INPUT</div>
      <div data-copy style={{fontSize:58,lineHeight:1.25,fontWeight:700}}>{scene.left}</div>
    </Panel></Reveal>
    <div style={{height:95,display:"flex",alignItems:"center",justifyContent:"center"}}>
      <div style={{width:4,height:60,background:c.cyan,transformOrigin:"top",transform:`scaleY(${interpolate(frame,[0,24],[0,1],clamp)})`}}/>
    </div>
    <Reveal delay={14}><Panel color={c.amber} theme={c}>
      <div style={{fontSize:30,color:c.amber,marginBottom:15}}>OUTCOME</div>
      <div data-copy style={{fontSize:58,lineHeight:1.25,fontWeight:700,color:c.amber}}>{scene.right}</div>
    </Panel></Reveal>
    <Reveal delay={24}><p data-copy style={{fontSize:48,lineHeight:1.32,color:c.cyan,marginTop:40,fontWeight:700}}>{scene.note}</p></Reveal>
  </AbsoluteFill>;
};

const ContentVideo:React.FC<Props> = ({video}) => {
  const frame=useCurrentFrame();const {width}=useVideoConfig();const scale=width/1080;
  const [handle]=useState(()=>delayRender("Loading licensed engine fonts"));
  const [fontsReady,setFontsReady]=useState(false);
  useEffect(()=>{
    Promise.all([new FontFace("EngineVera",`url(${staticFile("fonts/Vera.ttf")})`),new FontFace("EngineVera",`url(${staticFile("fonts/VeraBd.ttf")})`,{weight:"700"})].map(f=>f.load().then(loaded=>document.fonts.add(loaded))))
      .then(()=>document.fonts.ready).then(()=>{setFontsReady(true);continueRender(handle);}).catch(cancelRender);
  },[handle]);
  useLayoutEffect(()=>{
    if (!fontsReady) return;
    for (const el of document.querySelectorAll<HTMLElement>("[data-copy]")) {
      const rect=el.getBoundingClientRect();
      if(el.scrollWidth>el.clientWidth+1 || rect.left<70*scale || rect.right>1010*scale || rect.bottom>1510*scale) {
        cancelRender(new Error("Video copy exceeds the safe area; shorten the scene text"));
      }
    }
    const subtitle=document.querySelector<HTMLElement>("[data-subtitle]");
    if (subtitle && (subtitle.scrollWidth>subtitle.clientWidth+1 || subtitle.getBoundingClientRect().bottom>1721*scale)) {
      cancelRender(new Error("Subtitle exceeds its safe area; split the phrase"));
    }
  },[frame,fontsReady,scale]);
  const cue=video.captions.find(x=>frame>=x.fromFrame&&frame<x.toFrame);const c=video.theme;
  return <AbsoluteFill style={{background:c.bg,overflow:"hidden"}}><div style={{position:"absolute",width:1080,height:1920,transform:`scale(${scale})`,transformOrigin:"top left",color:c.white,fontFamily:"EngineVera, sans-serif"}}>
    <AbsoluteFill style={{backgroundImage:`linear-gradient(${c.cyan}06 1px,transparent 1px),linear-gradient(90deg,${c.cyan}06 1px,transparent 1px)`,backgroundSize:"90px 90px",transform:`translateY(${frame*.035}px)`}}/>
    {video.scenes.map((scene,index)=><Sequence key={scene.startFrame} from={scene.startFrame} durationInFrames={scene.durationInFrames}>
      <MotionScene scene={scene} index={index} video={video}/><Audio src={staticFile(scene.audio)}/>
    </Sequence>)}
    {cue&&<div data-subtitle style={{position:"absolute",left:76,right:76,bottom:200,padding:"22px 20px",background:"#020812",border:`1px solid ${c.line}`,borderRadius:12,color:c.white,fontSize:48,fontWeight:700,lineHeight:1.28,whiteSpace:"pre",textAlign:"center"}}>{cue.text}</div>}
    <div style={{position:"absolute",left:76,right:76,bottom:86}}>
      <div style={{display:"flex",gap:10,marginBottom:25}}>{video.scenes.map(scene=><div key={scene.startFrame} style={{height:5,flex:1,background:c.line,overflow:"hidden"}}><div style={{height:"100%",background:c.cyan,width:`${interpolate(frame,[scene.startFrame,scene.startFrame+scene.durationInFrames],[0,100],clamp)}%`}}/></div>)}</div>
      <div style={{display:"flex",justifyContent:"space-between",gap:20,fontSize:24,color:c.muted}}><span>{video.footer}</span><span>{Math.floor(frame/video.fps)}s</span></div>
    </div>
  </div></AbsoluteFill>;
};
const placeholder:Video={title:"Synthetic placeholder",exampleLabel:"SYNTHETIC DEMO",footer:"Supply a prepared render job",width:1080,height:1920,fps:30,durationInFrames:900,theme:{bg:"#07111F",panel:"#0D1D30",line:"#607D98",white:"#F0F6FC",muted:"#C1D0DF",cyan:"#62E8EF",amber:"#FFBD69"},scenes:[],captions:[]};
export const Root:React.FC = () => <Composition id="ContentVideo" component={ContentVideo} durationInFrames={900} fps={30} width={1080} height={1920} defaultProps={{video:placeholder}} calculateMetadata={({props})=>({durationInFrames:props.video.durationInFrames,fps:props.video.fps,width:props.video.width,height:props.video.height})}/>;
