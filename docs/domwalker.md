---
layout: default
---

# domwalker #

## Messages ##

### release ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>release</td>
</tr>

</table>

### pick ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>pick</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

<tr>
<td>newParents</td>
<td>array:domnode</td>
</tr>

</table>

### cancelPick ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>cancelPick</td>
</tr>

</table>

### highlight ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>highlight</td>
</tr>

<tr>
<td>node</td>
<td>nullable:domnode</td>
</tr>

</table>

### document ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>document</td>
</tr>

<tr>
<td>node</td>
<td>nullable:domnode</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

</table>

### documentElement ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>documentElement</td>
</tr>

<tr>
<td>node</td>
<td>nullable:domnode</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

</table>

### parents ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>parents</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

<tr>
<td>sameDocument</td>
<td>primitive</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>nodes</td>
<td>array:domnode</td>
</tr>

</table>

### retainNode ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>retainNode</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

</table>

### unretainNode ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>unretainNode</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

</table>

### releaseNode ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>releaseNode</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

<tr>
<td>force</td>
<td>primitive</td>
</tr>

</table>

### children ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>children</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

<tr>
<td>center</td>
<td>domnode</td>
</tr>

<tr>
<td>start</td>
<td>domnode</td>
</tr>

<tr>
<td>maxNodes</td>
<td>primitive</td>
</tr>

<tr>
<td>whatToShow</td>
<td>primitive</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>nodes</td>
<td>array:domnode</td>
</tr>

</table>

### siblings ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>siblings</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

<tr>
<td>center</td>
<td>domnode</td>
</tr>

<tr>
<td>start</td>
<td>domnode</td>
</tr>

<tr>
<td>maxNodes</td>
<td>primitive</td>
</tr>

<tr>
<td>whatToShow</td>
<td>primitive</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>nodes</td>
<td>array:domnode</td>
</tr>

</table>

### nextSibling ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>nextSibling</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

<tr>
<td>whatToShow</td>
<td>primitive</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>node</td>
<td>nullable:domnode</td>
</tr>

</table>

### previousSibling ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>previousSibling</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

<tr>
<td>whatToShow</td>
<td>primitive</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>node</td>
<td>nullable:domnode</td>
</tr>

</table>

### querySelector ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>querySelector</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

<tr>
<td>selector</td>
<td>primitive</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

<tr>
<td>newParents</td>
<td>array:domnode</td>
</tr>

</table>

### querySelectorAll ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>querySelectorAll</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

<tr>
<td>selector</td>
<td>primitive</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>list</td>
<td>domnodelist</td>
</tr>

</table>

### getSuggestionsForQuery ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>getSuggestionsForQuery</td>
</tr>

<tr>
<td>query</td>
<td>primitive</td>
</tr>

<tr>
<td>completing</td>
<td>primitive</td>
</tr>

<tr>
<td>selectorState</td>
<td>primitive</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>list</td>
<td>array:array:string</td>
</tr>

</table>

### addPseudoClassLock ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>addPseudoClassLock</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

<tr>
<td>pseudoClass</td>
<td>primitive</td>
</tr>

<tr>
<td>parents</td>
<td>primitive</td>
</tr>

</table>

### hideNode ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>hideNode</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

</table>

### unhideNode ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>unhideNode</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

</table>

### removePseudoClassLock ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>removePseudoClassLock</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

<tr>
<td>pseudoClass</td>
<td>primitive</td>
</tr>

<tr>
<td>parents</td>
<td>primitive</td>
</tr>

</table>

### clearPseudoClassLocks ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>clearPseudoClassLocks</td>
</tr>

<tr>
<td>node</td>
<td>nullable:domnode</td>
</tr>

</table>

### innerHTML ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>innerHTML</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>value</td>
<td>longstring</td>
</tr>

</table>

### outerHTML ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>outerHTML</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>value</td>
<td>longstring</td>
</tr>

</table>

### setOuterHTML ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>setOuterHTML</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

<tr>
<td>value</td>
<td>primitive</td>
</tr>

</table>

### removeNode ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>removeNode</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>nextSibling</td>
<td>nullable:domnode</td>
</tr>

</table>

### insertBefore ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>insertBefore</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

<tr>
<td>sibling</td>
<td>nullable:domnode</td>
</tr>

<tr>
<td>parent</td>
<td>domnode</td>
</tr>

</table>

### getMutations ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>getMutations</td>
</tr>

<tr>
<td>cleanup</td>
<td>primitive</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>mutations</td>
<td>array:dommutation</td>
</tr>

</table>

### isInDOMTree ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>isInDOMTree</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>attached</td>
<td>boolean</td>
</tr>

</table>

### getNodeActorFromObjectActor ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>getNodeActorFromObjectActor</td>
</tr>

<tr>
<td>objectActorID</td>
<td>string</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>nodeFront</td>
<td>nullable:disconnectedNode</td>
</tr>

</table>

### getStyleSheetOwnerNode ###

<table>

<tr>
<td>to</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>getStyleSheetOwnerNode</td>
</tr>

<tr>
<td>styleSheetActorID</td>
<td>string</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>ownerNode</td>
<td>nullable:disconnectedNode</td>
</tr>

</table>

## Events ##

### picker-node-hovered ###

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>pickerNodeHovered</td>
</tr>

<tr>
<td>node</td>
<td>disconnectedNode</td>
</tr>

</table>

### new-mutations ###

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>newMutations</td>
</tr>

</table>

### picker-node-picked ###

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>pickerNodePicked</td>
</tr>

<tr>
<td>node</td>
<td>disconnectedNode</td>
</tr>

</table>

### highlighter-ready ###

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>highlighter-ready</td>
</tr>

</table>

### highlighter-hide ###

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>highlighter-hide</td>
</tr>

</table>

### display-change ###

<table>

<tr>
<td>from</td>
<td>domwalker</td>
</tr>

<tr>
<td>type</td>
<td>display-change</td>
</tr>

<tr>
<td>nodes</td>
<td>array:domnode</td>
</tr>

</table>
