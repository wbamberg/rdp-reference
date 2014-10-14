---
layout: default
---

# domnodelist #

## Messages ##

### item ###

<table>

<tr>
<td>to</td>
<td>domnodelist</td>
</tr>

<tr>
<td>type</td>
<td>item</td>
</tr>

<tr>
<td>item</td>
<td>primitive</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domnodelist</td>
</tr>

<tr>
<td>node</td>
<td>domnode</td>
</tr>

<tr>
<td>newParents</td>
<td>array:domnode</td>
</tr>

</table>

### items ###

<table>

<tr>
<td>to</td>
<td>domnodelist</td>
</tr>

<tr>
<td>type</td>
<td>items</td>
</tr>

<tr>
<td>start</td>
<td>nullable:number</td>
</tr>

<tr>
<td>end</td>
<td>nullable:number</td>
</tr>

</table>

#### Response ####

<table>

<tr>
<td>from</td>
<td>domnodelist</td>
</tr>

<tr>
<td>nodes</td>
<td>array:domnode</td>
</tr>

<tr>
<td>newParents</td>
<td>array:domnode</td>
</tr>

</table>

### release ###

<table>

<tr>
<td>to</td>
<td>domnodelist</td>
</tr>

<tr>
<td>type</td>
<td>release</td>
</tr>

</table>

## Events ##
