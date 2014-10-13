---
---

# framerate #

## Messages ##

### startRecording ###

#### Request ####

<table>

<tr>
<td>to</td>
<td>framerate</td>
</tr>

<tr>
<td>type</td>
<td>startRecording</td>
</tr>

</table>

### stopRecording ###

#### Request ####

<table>

<tr>
<td>to</td>
<td>framerate</td>
</tr>

<tr>
<td>type</td>
<td>stopRecording</td>
</tr>

<tr>
<td>endAt</td>
<td>nullable:number</td>
</tr>

<tr>
<td>beginAt</td>
<td>nullable:number</td>
</tr>

</table>

#### Response ####
array:number

### cancelRecording ###

#### Request ####

<table>

<tr>
<td>to</td>
<td>framerate</td>
</tr>

<tr>
<td>type</td>
<td>cancelRecording</td>
</tr>

</table>

### isRecording ###

#### Request ####

<table>

<tr>
<td>to</td>
<td>framerate</td>
</tr>

<tr>
<td>type</td>
<td>isRecording</td>
</tr>

</table>

#### Response ####
boolean

### getPendingTicks ###

#### Request ####

<table>

<tr>
<td>to</td>
<td>framerate</td>
</tr>

<tr>
<td>type</td>
<td>getPendingTicks</td>
</tr>

<tr>
<td>endAt</td>
<td>nullable:number</td>
</tr>

<tr>
<td>beginAt</td>
<td>nullable:number</td>
</tr>

</table>

#### Response ####
array:number
