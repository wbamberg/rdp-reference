---
layout: default
---

# framerate #

## Messages ##

### startRecording ###

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
<td>Null or number</td>
</tr>

<tr>
<td>beginAt</td>
<td>Null or number</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>framerate</td>
</tr>

<tr>
<td>ticks</td>
<td>Array of number</td>
</tr>

</table>

### cancelRecording ###

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

<table>

<tr>
<td>from</td>
<td>framerate</td>
</tr>

<tr>
<td>recording</td>
<td>boolean</td>
</tr>

</table>

### getPendingTicks ###

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
<td>Null or number</td>
</tr>

<tr>
<td>beginAt</td>
<td>Null or number</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>framerate</td>
</tr>

<tr>
<td>ticks</td>
<td>Array of number</td>
</tr>

</table>
