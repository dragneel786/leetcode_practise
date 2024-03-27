<h2><a href="https://leetcode.com/problems/count-unhappy-friends/">1583. Count Unhappy Friends</a></h2><h3>Medium</h3><hr><div element-id="906"><p element-id="905">You are given a list of&nbsp;<code element-id="904">preferences</code>&nbsp;for&nbsp;<code element-id="903">n</code>&nbsp;friends, where <code element-id="902">n</code> is always <strong element-id="901">even</strong>.</p>

<p element-id="900">For each person <code element-id="899">i</code>,&nbsp;<code element-id="898">preferences[i]</code>&nbsp;contains&nbsp;a list of friends&nbsp;<strong element-id="897">sorted</strong> in the <strong element-id="896">order of preference</strong>. In other words, a friend earlier in the list is more preferred than a friend later in the list.&nbsp;Friends in&nbsp;each list are&nbsp;denoted by integers from <code element-id="895">0</code> to <code element-id="894">n-1</code>.</p>

<p element-id="893">All the friends are divided into pairs.&nbsp;The pairings are&nbsp;given in a list&nbsp;<code element-id="892">pairs</code>,&nbsp;where <code element-id="891">pairs[i] = [x<sub element-id="890">i</sub>, y<sub element-id="889">i</sub>]</code> denotes <code element-id="888">x<sub element-id="887">i</sub></code>&nbsp;is paired with <code element-id="886">y<sub element-id="885">i</sub></code> and <code element-id="884">y<sub element-id="883">i</sub></code> is paired with <code element-id="882">x<sub element-id="881">i</sub></code>.</p>

<p element-id="880">However, this pairing may cause some of the friends to be unhappy.&nbsp;A friend <code element-id="879">x</code>&nbsp;is unhappy if <code element-id="878">x</code>&nbsp;is paired with <code element-id="877">y</code>&nbsp;and there exists a friend <code element-id="876">u</code>&nbsp;who&nbsp;is paired with <code element-id="875">v</code>&nbsp;but:</p>

<ul element-id="874">
	<li element-id="873"><code element-id="872">x</code>&nbsp;prefers <code element-id="871">u</code>&nbsp;over <code element-id="870">y</code>,&nbsp;and</li>
	<li element-id="869"><code element-id="868">u</code>&nbsp;prefers <code element-id="867">x</code>&nbsp;over <code element-id="866">v</code>.</li>
</ul>

<p element-id="865">Return <em element-id="864">the number of unhappy friends</em>.</p>

<p element-id="863">&nbsp;</p>
<p element-id="862"><strong class="example" element-id="861">Example 1:</strong></p>

<pre element-id="860"><strong element-id="859">Input:</strong> n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]
<strong element-id="858">Output:</strong> 2
<strong element-id="857">Explanation:</strong>
Friend 1 is unhappy because:
- 1 is paired with 0 but prefers 3 over 0, and
- 3 prefers 1 over 2.
Friend 3 is unhappy because:
- 3 is paired with 2 but prefers 1 over 2, and
- 1 prefers 3 over 0.
Friends 0 and 2 are happy.
</pre>

<p element-id="856"><strong class="example" element-id="855">Example 2:</strong></p>

<pre element-id="854"><strong element-id="853">Input:</strong> n = 2, preferences = [[1], [0]], pairs = [[1, 0]]
<strong element-id="852">Output:</strong> 0
<strong element-id="851">Explanation:</strong> Both friends 0 and 1 are happy.
</pre>

<p element-id="850"><strong class="example" element-id="849">Example 3:</strong></p>

<pre element-id="848"><strong element-id="847">Input:</strong> n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]
<strong element-id="846">Output:</strong> 4
</pre>

<p element-id="845">&nbsp;</p>
<p element-id="844"><strong element-id="843">Constraints:</strong></p>

<ul element-id="842">
	<li element-id="841"><code element-id="840">2 &lt;= n &lt;= 500</code></li>
	<li element-id="839"><code element-id="838">n</code>&nbsp;is even.</li>
	<li element-id="837"><code element-id="836">preferences.length&nbsp;== n</code></li>
	<li element-id="835"><code element-id="834">preferences[i].length&nbsp;== n - 1</code></li>
	<li element-id="833"><code element-id="832">0 &lt;= preferences[i][j] &lt;= n - 1</code></li>
	<li element-id="831"><code element-id="830">preferences[i]</code>&nbsp;does not contain <code element-id="829">i</code>.</li>
	<li element-id="828">All values in&nbsp;<code element-id="827">preferences[i]</code>&nbsp;are unique.</li>
	<li element-id="826"><code element-id="825">pairs.length&nbsp;== n/2</code></li>
	<li element-id="824"><code element-id="823">pairs[i].length&nbsp;== 2</code></li>
	<li element-id="822"><code element-id="821">x<sub element-id="820">i</sub> != y<sub element-id="819">i</sub></code></li>
	<li element-id="818"><code element-id="817">0 &lt;= x<sub element-id="816">i</sub>, y<sub element-id="815">i</sub>&nbsp;&lt;= n - 1</code></li>
	<li element-id="814">Each person is contained in <strong element-id="813">exactly one</strong> pair.</li>
</ul>
</div>