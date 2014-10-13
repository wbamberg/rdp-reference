---
---

# domnode #

## Messages ##

### getNodeValue ###

#### Request ####

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
longstring

### setNodeValue ###

#### Request ####

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

#### Request ####

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
<td>nullable:number</td>
</tr>

</table>

### getEventListenerInfo ###

#### Request ####

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
json

### modifyAttributes ###

#### Request ####

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
<td>array:json</td>
</tr>

</table>

### getFontFamilyDataURL ###

#### Request ####

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
<td>nullable:string</td>
</tr>

</table>
