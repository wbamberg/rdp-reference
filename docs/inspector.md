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

<table>

<tr>
<td>from</td>
<td>inspector</td>
</tr>

<tr>
<td>walker</td>
<td>domwalker</td>
</tr>

</table>

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

<table>

<tr>
<td>from</td>
<td>inspector</td>
</tr>

<tr>
<td>pageStyle</td>
<td>pagestyle</td>
</tr>

</table>

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

<table>

<tr>
<td>from</td>
<td>inspector</td>
</tr>

<tr>
<td>highligter</td>
<td>highlighter</td>
</tr>

</table>

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

<table>

<tr>
<td>from</td>
<td>inspector</td>
</tr>

<tr>
<td>highlighter</td>
<td>nullable:customhighlighter</td>
</tr>

</table>

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

#### Response ####

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
