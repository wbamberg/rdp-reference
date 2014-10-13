
# inspector #

## Messages ##

### getWalker ###

#### Request ####

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

#### Request ####

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

#### Request ####

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

#### Request ####

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

#### Request ####

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
