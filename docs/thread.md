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
array:chromium_source

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
array:chromium_frame

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
<td>nullable:string</td>
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
<td>nullable:json</td>
</tr>

<tr>
<td>actor</td>
<td>chromium_breakpoint#actorid</td>
</tr>

</table>
