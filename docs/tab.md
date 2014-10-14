---
layout: default
---

# tab #

## Messages ##

### attach ###

<table>

<tr>
<td>to</td>
<td>tab</td>
</tr>

<tr>
<td>type</td>
<td>attach</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>tab</td>
</tr>

<tr>
<td>threadActor</td>
<td>chromium_thread#actorid</td>
</tr>

<tr>
<td>type</td>
<td>tabAttached</td>
</tr>

</table>

### navigateTo ###

<table>

<tr>
<td>to</td>
<td>tab</td>
</tr>

<tr>
<td>type</td>
<td>navigateTo</td>
</tr>

<tr>
<td>url</td>
<td>string</td>
</tr>

</table>

### reload ###

<table>

<tr>
<td>to</td>
<td>tab</td>
</tr>

<tr>
<td>type</td>
<td>reload</td>
</tr>

<tr>
<td>options</td>
<td>nullable:json</td>
</tr>

</table>

### reconfigure ###

<table>

<tr>
<td>to</td>
<td>tab</td>
</tr>

<tr>
<td>type</td>
<td>reconfigure</td>
</tr>

<tr>
<td>options</td>
<td>nullable:json</td>
</tr>

</table>

### detach ###

<table>

<tr>
<td>to</td>
<td>tab</td>
</tr>

<tr>
<td>type</td>
<td>detach</td>
</tr>

</table>

## Events ##

### tab-navigated ###

<table>

<tr>
<td>from</td>
<td>tab</td>
</tr>

<tr>
<td>type</td>
<td>tabNavigated</td>
</tr>

<tr>
<td>url</td>
<td>string</td>
</tr>

<tr>
<td>nativeConsoleAPI</td>
<td>True</td>
</tr>

<tr>
<td>state</td>
<td>string</td>
</tr>

</table>
