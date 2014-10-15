---
layout: default
---

# cssUsage #

## Messages ##

### start ###

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

<table>

<tr>
<td>from</td>
<td>cssUsage</td>
</tr>

<tr>
<td>reports</td>
<td>Array of json</td>
</tr>

</table>

### createPageReport ###

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

#### Response ####
json

### _testOnly_visitedPages ###

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

<table>

<tr>
<td>from</td>
<td>cssUsage</td>
</tr>

<tr>
<td>value</td>
<td>Array of string</td>
</tr>

</table>

## Events ##

### state-change ###

<table>

<tr>
<td>from</td>
<td>cssUsage</td>
</tr>

<tr>
<td>type</td>
<td>stateChange</td>
</tr>

<tr>
<td>stateChange</td>
<td>json</td>
</tr>

</table>
