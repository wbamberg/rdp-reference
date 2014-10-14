---
layout: default
---

# inspector #

## Messages ##

### getWalker ###

<table>

<tr>
<td>to</td>
<td>inspector</td>
</tr>

<tr>
<td>type</td>
<td>getWalker</td>
</tr>

</table>

#### Response ####
domwalker

### getPageStyle ###

<table>

<tr>
<td>to</td>
<td>inspector</td>
</tr>

<tr>
<td>type</td>
<td>getPageStyle</td>
</tr>

</table>

#### Response ####
pagestyle

### getHighlighter ###

<table>

<tr>
<td>to</td>
<td>inspector</td>
</tr>

<tr>
<td>type</td>
<td>getHighlighter</td>
</tr>

<tr>
<td>autohide</td>
<td>boolean</td>
</tr>

</table>

#### Response ####
highlighter

### getHighlighterByType ###

<table>

<tr>
<td>to</td>
<td>inspector</td>
</tr>

<tr>
<td>type</td>
<td>getHighlighterByType</td>
</tr>

<tr>
<td>typeName</td>
<td>primitive</td>
</tr>

</table>

#### Response ####
nullable:customhighlighter

### getImageDataFromURL ###

<table>

<tr>
<td>to</td>
<td>inspector</td>
</tr>

<tr>
<td>type</td>
<td>getImageDataFromURL</td>
</tr>

<tr>
<td>url</td>
<td>primitive</td>
</tr>

<tr>
<td>maxDim</td>
<td>nullable:number</td>
</tr>

</table>

<table>

<tr>
<td>from</td>
<td>inspector</td>
</tr>

<tr>
<td>data</td>
<td>nullable:longstring</td>
</tr>

<tr>
<td>size</td>
<td>json</td>
</tr>

</table>
