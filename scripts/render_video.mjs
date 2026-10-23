// Local rendering only. No model/browser downloads, cloud services or publication.
import {createServer} from "node:net";
import {createRequire} from "node:module";
import {existsSync, readFileSync} from "node:fs";
import path from "node:path";
import {fileURLToPath} from "node:url";
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const modules=process.env.CONTENT_AGENT_NODE_MODULES || path.join(root,"node_modules");
const require=createRequire(path.join(modules,"..","package.json"));
const {bundle}=require("@remotion/bundler");
const {selectComposition,renderMedia}=require("@remotion/renderer");
const job=path.resolve(process.argv[2] || "");
if (!job.startsWith(path.join(root,"out")+path.sep) || !existsSync(path.join(job,"timing.json"))) throw new Error("Pass a prepared job under out/");
const browserExecutable=process.env.CONTENT_AGENT_BROWSER;
if (!browserExecutable || !existsSync(browserExecutable)) throw new Error("Set CONTENT_AGENT_BROWSER to an installed Chrome/Chromium executable. No automatic browser download is permitted.");
const output=path.join(job,"motion.mp4");
if(existsSync(output)) throw new Error("Existing video preserved; use a new output_dir for a revision");
const video=JSON.parse(readFileSync(path.join(job,"timing.json"),"utf8"));
const serveUrl=await bundle({entryPoint:path.join(root,"src/index.ts"),rootDir:root,publicDir:path.join(job,"public"),outDir:path.join(job,"bundle"),enableCaching:false,gitSource:null,webpackOverride:config=>({...config,resolve:{...config.resolve,modules:[modules,...(config.resolve?.modules || ["node_modules"])]}})});
// Avoid a localhost IPv4/IPv6 collision with an unrelated development server.
const reservation=createServer();
await new Promise((resolve,reject)=>{reservation.once("error",reject);reservation.listen(0,"::",resolve);});
const port=reservation.address().port;
await new Promise((resolve,reject)=>reservation.close(error=>error?reject(error):resolve()));
const inputProps={video};
const composition=await selectComposition({serveUrl,id:"ContentVideo",inputProps,browserExecutable,port});
let last=-1;
await renderMedia({composition,serveUrl,inputProps,codec:"h264",pixelFormat:"yuv420p",audioCodec:"aac",enforceAudioTrack:true,crf:18,outputLocation:output,overwrite:false,concurrency:2,browserExecutable,port,onProgress:({progress})=>{const step=Math.floor(progress*10);if(step!==last){last=step;console.log(`Render ${step*10}%`);}}});
console.log("Rendered video; run the Python validate-video command for final QC.");
