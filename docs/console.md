---
---

# console #

## Messages ##

### startListeners ###

#### Request ####

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

#### Request ####

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

#### Request ####

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

#### Request ####

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

#### Request ####

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

### autocomplete ###

#### Request ####

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

#### Request ####

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

#### Request ####

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

#### Request ####

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
