---
layout: default
---

# pagestyle #

## Messages ##

### getComputed ###

<table>

<tr>
<td>to</td>
<td>pagestyle</td>
</tr>

<tr>
<td>type</td>
<td>getComputed</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

<tr>
<td>filter</td>
<td>string</td>
</tr>

<tr>
<td>markMatched</td>
<td>boolean</td>
</tr>

<tr>
<td>onlyMatched</td>
<td>boolean</td>
</tr>

</table>

#### Response ####
json

### getMatchedSelectors ###

<table>

<tr>
<td>to</td>
<td>pagestyle</td>
</tr>

<tr>
<td>type</td>
<td>getMatchedSelectors</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

<tr>
<td>filter</td>
<td>string</td>
</tr>

<tr>
<td>property</td>
<td>string</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>pagestyle</td>
</tr>

<tr>
<td>rules</td>
<td>array:domstylerule</td>
</tr>

<tr>
<td>sheets</td>
<td>array:stylesheet</td>
</tr>

<tr>
<td>matched</td>
<td>array:matchedselector</td>
</tr>

</table>

### getApplied ###

<table>

<tr>
<td>to</td>
<td>pagestyle</td>
</tr>

<tr>
<td>type</td>
<td>getApplied</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

<tr>
<td>filter</td>
<td>string</td>
</tr>

<tr>
<td>matchedSelectors</td>
<td>boolean</td>
</tr>

<tr>
<td>inherited</td>
<td>boolean</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>pagestyle</td>
</tr>

<tr>
<td>rules</td>
<td>array:domstylerule</td>
</tr>

<tr>
<td>sheets</td>
<td>array:stylesheet</td>
</tr>

<tr>
<td>entries</td>
<td>array:appliedstyle</td>
</tr>

</table>

### getLayout ###

<table>

<tr>
<td>to</td>
<td>pagestyle</td>
</tr>

<tr>
<td>type</td>
<td>getLayout</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

<tr>
<td>autoMargins</td>
<td>boolean</td>
</tr>

</table>

### addNewRule ###

<table>

<tr>
<td>to</td>
<td>pagestyle</td>
</tr>

<tr>
<td>type</td>
<td>addNewRule</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>pagestyle</td>
</tr>

<tr>
<td>rules</td>
<td>array:domstylerule</td>
</tr>

<tr>
<td>sheets</td>
<td>array:stylesheet</td>
</tr>

<tr>
<td>entries</td>
<td>array:appliedstyle</td>
</tr>

</table>
