---
layout: default
---

# console #

## Messages ##

### startListeners ###

<table>

<tr>
<td>to</td>
<td>console</td>
</tr>

<tr>
<td>type</td>
<td>startListeners</td>
</tr>

<tr>
<td>listeners</td>
<td>array:string</td>
</tr>

</table>

### stopListeners ###

<table>

<tr>
<td>to</td>
<td>console</td>
</tr>

<tr>
<td>type</td>
<td>stopListeners</td>
</tr>

<tr>
<td>listeners</td>
<td>array:string</td>
</tr>

</table>

### getCachedMessages ###

<table>

<tr>
<td>to</td>
<td>console</td>
</tr>

<tr>
<td>type</td>
<td>getCachedMessages</td>
</tr>

<tr>
<td>messageTypes</td>
<td>array:string</td>
</tr>

</table>

#### Response ####
array:chromium_consolemsg

### clearMessagesCache ###

<table>

<tr>
<td>to</td>
<td>console</td>
</tr>

<tr>
<td>type</td>
<td>clearMessagesCache</td>
</tr>

</table>

### evaluateJS ###

<table>

<tr>
<td>to</td>
<td>console</td>
</tr>

<tr>
<td>type</td>
<td>evaluateJS</td>
</tr>

<tr>
<td>text</td>
<td>string</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>console</td>
</tr>

<tr>
<td>result</td>
<td>nullable:chromium_grip</td>
</tr>

</table>

### autocomplete ###

<table>

<tr>
<td>to</td>
<td>console</td>
</tr>

<tr>
<td>type</td>
<td>autocomplete</td>
</tr>

<tr>
<td>cursor</td>
<td>number</td>
</tr>

<tr>
<td>text</td>
<td>string</td>
</tr>

</table>

### getPreferences ###

<table>

<tr>
<td>to</td>
<td>console</td>
</tr>

<tr>
<td>type</td>
<td>getPreferences</td>
</tr>

</table>

### setPreferences ###

<table>

<tr>
<td>to</td>
<td>console</td>
</tr>

<tr>
<td>type</td>
<td>setPreferences</td>
</tr>

</table>

### sendHTTPRequest ###

<table>

<tr>
<td>to</td>
<td>console</td>
</tr>

<tr>
<td>type</td>
<td>sendHTTPRequest</td>
</tr>

</table>
