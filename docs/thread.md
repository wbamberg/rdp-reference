---
layout: default
---

# thread #

## Messages ##

### reconfigure ###

<table>

<tr>
<td>to</td>
<td>thread</td>
</tr>

<tr>
<td>type</td>
<td>reconfigure</td>
</tr>

<tr>
<td>options</td>
<td>json</td>
</tr>

</table>

### attach ###

<table>

<tr>
<td>to</td>
<td>thread</td>
</tr>

<tr>
<td>type</td>
<td>attach</td>
</tr>

<tr>
<td>useSourceMaps</td>
<td>boolean</td>
</tr>

</table>

### interrupt ###

<table>

<tr>
<td>to</td>
<td>thread</td>
</tr>

<tr>
<td>type</td>
<td>interrupt</td>
</tr>

</table>

### resume ###

<table>

<tr>
<td>to</td>
<td>thread</td>
</tr>

<tr>
<td>type</td>
<td>resume</td>
</tr>

<tr>
<td>forceCompletion</td>
<td>json</td>
</tr>

<tr>
<td>resumeLimit</td>
<td>json</td>
</tr>

</table>

### sources ###

<table>

<tr>
<td>to</td>
<td>thread</td>
</tr>

<tr>
<td>type</td>
<td>sources</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>thread</td>
</tr>

<tr>
<td>sources</td>
<td>Array of source</td>
</tr>

</table>

### frames ###

<table>

<tr>
<td>to</td>
<td>thread</td>
</tr>

<tr>
<td>type</td>
<td>frames</td>
</tr>

<tr>
<td>count</td>
<td>number</td>
</tr>

<tr>
<td>start</td>
<td>number</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>thread</td>
</tr>

<tr>
<td>frames</td>
<td>Array of frame</td>
</tr>

</table>

### setBreakpoint ###

<table>

<tr>
<td>to</td>
<td>thread</td>
</tr>

<tr>
<td>type</td>
<td>setBreakpoint</td>
</tr>

<tr>
<td>location</td>
<td>json</td>
</tr>

<tr>
<td>condition</td>
<td>Null or string</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>thread</td>
</tr>

<tr>
<td>actualLocation</td>
<td>Null or json</td>
</tr>

<tr>
<td>actor</td>
<td>breakpoint#actorid</td>
</tr>

</table>

## Events ##

### paused ###

<table>

<tr>
<td>from</td>
<td>thread</td>
</tr>

<tr>
<td>type</td>
<td>paused</td>
</tr>

<tr>
<td>poppedFrames</td>
<td>Array of string</td>
</tr>

<tr>
<td>frame</td>
<td>frame</td>
</tr>

<tr>
<td>why</td>
<td>string</td>
</tr>

<tr>
<td>actor</td>
<td>pauseactor</td>
</tr>

</table>

### resumed ###

<table>

<tr>
<td>from</td>
<td>thread</td>
</tr>

<tr>
<td>type</td>
<td>resumed</td>
</tr>

</table>

### exited ###

<table>

<tr>
<td>from</td>
<td>thread</td>
</tr>

<tr>
<td>type</td>
<td>exited</td>
</tr>

</table>

### new-source ###

<table>

<tr>
<td>from</td>
<td>thread</td>
</tr>

<tr>
<td>type</td>
<td>newSource</td>
</tr>

<tr>
<td>source</td>
<td>source</td>
</tr>

</table>
