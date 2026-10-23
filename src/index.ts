import {createElement} from "react";
import {registerRoot} from "remotion";
import {Root} from "./Root";

// Keep the registration side effect separate from the editable composition catalog.
registerRoot(function ContentCatalog() {
  return createElement(Root);
});
