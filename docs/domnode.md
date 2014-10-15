---
layout: default
---

# domnode #

## Messages ##

### getNodeValue ###

<table>

<tr>
<td>to</td>
<td>domnode</td>
</tr>

<tr>
<td>type</td>
<td>getNodeValue</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domnode</td>
</tr>

<tr>
<td>value</td>
<td>longstring</td>
</tr>

</table>

### setNodeValue ###

<table>

<tr>
<td>to</td>
<td>domnode</td>
</tr>

<tr>
<td>type</td>
<td>setNodeValue</td>
</tr>

<tr>
<td>value</td>
<td>primitive</td>
</tr>

</table>

### getImageData ###

<table>

<tr>
<td>to</td>
<td>domnode</td>
</tr>

<tr>
<td>type</td>
<td>getImageData</td>
</tr>

<tr>
<td>maxDim</td>
<td>Null or number</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domnode</td>
</tr>

<tr>
<td>data</td>
<td>Null or longstring</td>
</tr>

<tr>
<td>size</td>
<td>json</td>
</tr>

</table>

### getEventListenerInfo ###

<table>

<tr>
<td>to</td>
<td>domnode</td>
</tr>

<tr>
<td>type</td>
<td>getEventListenerInfo</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domnode</td>
</tr>

<tr>
<td>events</td>
<td>json</td>
</tr>

</table>

### modifyAttributes ###

<table>

<tr>
<td>to</td>
<td>domnode</td>
</tr>

<tr>
<td>type</td>
<td>modifyAttributes</td>
</tr>

<tr>
<td>modifications</td>
<td>Array of json</td>
</tr>

</table>

### getFontFamilyDataURL ###

<table>

<tr>
<td>to</td>
<td>domnode</td>
</tr>

<tr>
<td>type</td>
<td>getFontFamilyDataURL</td>
</tr>

<tr>
<td>font</td>
<td>string</td>
</tr>

<tr>
<td>fillStyle</td>
<td>Null or string</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domnode</td>
</tr>

<tr>
<td>data</td>
<td>Null or longstring</td>
</tr>

<tr>
<td>size</td>
<td>json</td>
</tr>

</table>
