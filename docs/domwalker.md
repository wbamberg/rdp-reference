---
---

# domwalker #

## Messages ##

### release ###

#### Request ####

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

#### Request ####

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

### cancelPick ###

#### Request ####

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

#### Request ####

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

#### Request ####

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
domnode

### documentElement ###

#### Request ####

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
domnode

### parents ###

#### Request ####

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
array:domnode

### retainNode ###

#### Request ####

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

#### Request ####

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

#### Request ####

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

#### Request ####

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

### siblings ###

#### Request ####

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

### nextSibling ###

#### Request ####

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
nullable:domnode

### previousSibling ###

#### Request ####

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
nullable:domnode

### querySelector ###

#### Request ####

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

### querySelectorAll ###

#### Request ####

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
domnodelist

### getSuggestionsForQuery ###

#### Request ####

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
array:array:string

### addPseudoClassLock ###

#### Request ####

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

#### Request ####

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

#### Request ####

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

#### Request ####

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

#### Request ####

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

#### Request ####

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
longstring

### outerHTML ###

#### Request ####

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
longstring

### setOuterHTML ###

#### Request ####

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

#### Request ####

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
nullable:domnode

### insertBefore ###

#### Request ####

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

#### Request ####

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
array:dommutation

### isInDOMTree ###

#### Request ####

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
boolean

### getNodeActorFromObjectActor ###

#### Request ####

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
nullable:disconnectedNode

### getStyleSheetOwnerNode ###

#### Request ####

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
nullable:disconnectedNode
