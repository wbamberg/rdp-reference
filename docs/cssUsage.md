---
---

# cssUsage #

## Messages ##

### start ###

#### Request ####

<table>

<tr>
<td>to</td>
<td>cssUsage</td>
</tr>

<tr>
<td>type</td>
<td>start</td>
</tr>

<tr>
<td>url</td>
<td>boolean</td>
</tr>

</table>

### stop ###

#### Request ####

<table>

<tr>
<td>to</td>
<td>cssUsage</td>
</tr>

<tr>
<td>type</td>
<td>stop</td>
</tr>

</table>

### toggle ###

#### Request ####

<table>

<tr>
<td>to</td>
<td>cssUsage</td>
</tr>

<tr>
<td>type</td>
<td>toggle</td>
</tr>

</table>

### oneshot ###

#### Request ####

<table>

<tr>
<td>to</td>
<td>cssUsage</td>
</tr>

<tr>
<td>type</td>
<td>oneshot</td>
</tr>

</table>

### createEditorReport ###

#### Request ####

<table>

<tr>
<td>to</td>
<td>cssUsage</td>
</tr>

<tr>
<td>type</td>
<td>createEditorReport</td>
</tr>

<tr>
<td>url</td>
<td>string</td>
</tr>

</table>

#### Response ####
array:json

### createPageReport ###

#### Request ####

<table>

<tr>
<td>to</td>
<td>cssUsage</td>
</tr>

<tr>
<td>type</td>
<td>createPageReport</td>
</tr>

</table>

### _testOnly_visitedPages ###

#### Request ####

<table>

<tr>
<td>to</td>
<td>cssUsage</td>
</tr>

<tr>
<td>type</td>
<td>_testOnly_visitedPages</td>
</tr>

</table>

#### Response ####
array:string
