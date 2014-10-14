---
layout: default
---

# preference #

## Messages ##

### getBoolPref ###

#### Request ####

<table>

<tr>
<td>to</td>
<td>preference</td>
</tr>

<tr>
<td>type</td>
<td>getBoolPref</td>
</tr>

<tr>
<td>value</td>
<td>primitive</td>
</tr>

</table>

#### Response ####
boolean

### getCharPref ###

#### Request ####

<table>

<tr>
<td>to</td>
<td>preference</td>
</tr>

<tr>
<td>type</td>
<td>getCharPref</td>
</tr>

<tr>
<td>value</td>
<td>primitive</td>
</tr>

</table>

#### Response ####
string

### getIntPref ###

#### Request ####

<table>

<tr>
<td>to</td>
<td>preference</td>
</tr>

<tr>
<td>type</td>
<td>getIntPref</td>
</tr>

<tr>
<td>value</td>
<td>primitive</td>
</tr>

</table>

#### Response ####
number

### getAllPrefs ###

#### Request ####

<table>

<tr>
<td>to</td>
<td>preference</td>
</tr>

<tr>
<td>type</td>
<td>getAllPrefs</td>
</tr>

</table>

#### Response ####
json

### setBoolPref ###

#### Request ####

<table>

<tr>
<td>to</td>
<td>preference</td>
</tr>

<tr>
<td>type</td>
<td>setBoolPref</td>
</tr>

<tr>
<td>name</td>
<td>primitive</td>
</tr>

<tr>
<td>value</td>
<td>primitive</td>
</tr>

</table>

### setCharPref ###

#### Request ####

<table>

<tr>
<td>to</td>
<td>preference</td>
</tr>

<tr>
<td>type</td>
<td>setCharPref</td>
</tr>

<tr>
<td>name</td>
<td>primitive</td>
</tr>

<tr>
<td>value</td>
<td>primitive</td>
</tr>

</table>

### setIntPref ###

#### Request ####

<table>

<tr>
<td>to</td>
<td>preference</td>
</tr>

<tr>
<td>type</td>
<td>setIntPref</td>
</tr>

<tr>
<td>name</td>
<td>primitive</td>
</tr>

<tr>
<td>value</td>
<td>primitive</td>
</tr>

</table>

### clearUserPref ###

#### Request ####

<table>

<tr>
<td>to</td>
<td>preference</td>
</tr>

<tr>
<td>type</td>
<td>clearUserPref</td>
</tr>

<tr>
<td>name</td>
<td>primitive</td>
</tr>

</table>
