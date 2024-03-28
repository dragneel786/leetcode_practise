<h2><a href="https://leetcode.com/problems/find-the-punishment-number-of-an-integer/">2698. Find the Punishment Number of an Integer</a></h2><h3>Medium</h3><hr><div element-id="882"><p element-id="881">Given a positive integer <code element-id="880">n</code>, return <em element-id="879">the <strong element-id="878">punishment number</strong></em> of <code element-id="877">n</code>.</p>

<p element-id="876">The <strong element-id="875">punishment number</strong> of <code element-id="874">n</code> is defined as the sum of the squares of all integers <code element-id="873">i</code> such that:</p>

<ul element-id="872">
	<li element-id="871"><code element-id="870">1 &lt;= i &lt;= n</code></li>
	<li element-id="869">The decimal representation of <code element-id="868">i * i</code> can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals <code element-id="867">i</code>.</li>
</ul>

<p element-id="866">&nbsp;</p>
<p element-id="865"><strong class="example" element-id="864">Example 1:</strong></p>

<pre element-id="863"><strong element-id="862">Input:</strong> n = 10
<strong element-id="861">Output:</strong> 182
<strong element-id="860">Explanation:</strong> There are exactly 3 integers i that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 + 1.
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 + 0.
Hence, the punishment number of 10 is 1 + 81 + 100 = 182
</pre>

<p element-id="859"><strong class="example" element-id="858">Example 2:</strong></p>

<pre element-id="857"><strong element-id="856">Input:</strong> n = 37
<strong element-id="855">Output:</strong> 1478
<strong element-id="854">Explanation:</strong> There are exactly 4 integers i that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1. 
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 + 1. 
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 + 0. 
- 36 since 36 * 36 = 1296 and 1296 can be partitioned into 1 + 29 + 6.
Hence, the punishment number of 37 is 1 + 81 + 100 + 1296 = 1478
</pre>

<p element-id="853">&nbsp;</p>
<p element-id="852"><strong element-id="851">Constraints:</strong></p>

<ul element-id="850">
	<li element-id="849"><code element-id="848">1 &lt;= n &lt;= 1000</code></li>
</ul>
</div>