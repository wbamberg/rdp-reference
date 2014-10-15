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
<td>Array of string</td>
</tr>

</table>

#### Response ####
json

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
<td>Array of string</td>
</tr>

</table>

#### Response ####
json

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
<td>Array of string</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>console</td>
</tr>

<tr>
<td>messages</td>
<td>Array of consolemsg</td>
</tr>

</table>

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
<td>Null or grip</td>
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

#### Response ####
json

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

## Events ##

### ConsoleAPI ###

<table>

<tr>
<td>from</td>
<td>console</td>
</tr>

<tr>
<td>type</td>
<td>consoleAPICall</td>
</tr>

<tr>
<td>message</td>
<td>consolemsg</td>
</tr>

</table>
