---
layout: default
---

# stylesheet #

## Messages ##

### toggleDisabled ###

<table>

<tr>
<td>to</td>
<td>stylesheet</td>
</tr>

<tr>
<td>type</td>
<td>toggleDisabled</td>
</tr>

</table>

#### Response ####
boolean

### getText ###

<table>

<tr>
<td>to</td>
<td>stylesheet</td>
</tr>

<tr>
<td>type</td>
<td>getText</td>
</tr>

</table>

#### Response ####
longstring

### getOriginalSources ###

<table>

<tr>
<td>to</td>
<td>stylesheet</td>
</tr>

<tr>
<td>type</td>
<td>getOriginalSources</td>
</tr>

</table>

#### Response ####
nullable:array:originalsource

### getOriginalLocation ###

<table>

<tr>
<td>to</td>
<td>stylesheet</td>
</tr>

<tr>
<td>type</td>
<td>getOriginalLocation</td>
</tr>

<tr>
<td>column</td>
<td>number</td>
</tr>

<tr>
<td>line</td>
<td>number</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>stylesheet</td>
</tr>

<tr>
<td>column</td>
<td>number</td>
</tr>

<tr>
<td>source</td>
<td>string</td>
</tr>

<tr>
<td>line</td>
<td>number</td>
</tr>

</table>

### getMediaRules ###

<table>

<tr>
<td>to</td>
<td>stylesheet</td>
</tr>

<tr>
<td>type</td>
<td>getMediaRules</td>
</tr>

</table>

#### Response ####
nullable:array:mediarule

### update ###

<table>

<tr>
<td>to</td>
<td>stylesheet</td>
</tr>

<tr>
<td>type</td>
<td>update</td>
</tr>

<tr>
<td>text</td>
<td>string</td>
</tr>

<tr>
<td>transition</td>
<td>boolean</td>
</tr>

</table>
