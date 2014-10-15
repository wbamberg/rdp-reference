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

<table>

<tr>
<td>from</td>
<td>stylesheet</td>
</tr>

<tr>
<td>disabled</td>
<td>boolean</td>
</tr>

</table>

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

<table>

<tr>
<td>from</td>
<td>stylesheet</td>
</tr>

<tr>
<td>text</td>
<td>longstring</td>
</tr>

</table>

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

<table>

<tr>
<td>from</td>
<td>stylesheet</td>
</tr>

<tr>
<td>originalSources</td>
<td>Null or Array of originalsource</td>
</tr>

</table>

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

<table>

<tr>
<td>from</td>
<td>stylesheet</td>
</tr>

<tr>
<td>mediaRules</td>
<td>Null or Array of mediarule</td>
</tr>

</table>

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

## Events ##

### style-applied ###

<table>

<tr>
<td>from</td>
<td>stylesheet</td>
</tr>

<tr>
<td>type</td>
<td>styleApplied</td>
</tr>

</table>

### property-change ###

<table>

<tr>
<td>from</td>
<td>stylesheet</td>
</tr>

<tr>
<td>type</td>
<td>propertyChange</td>
</tr>

<tr>
<td>property</td>
<td>string</td>
</tr>

<tr>
<td>value</td>
<td>json</td>
</tr>

</table>

### media-rules-changed ###

<table>

<tr>
<td>from</td>
<td>stylesheet</td>
</tr>

<tr>
<td>type</td>
<td>mediaRulesChanged</td>
</tr>

<tr>
<td>rules</td>
<td>Array of mediarule</td>
</tr>

</table>
