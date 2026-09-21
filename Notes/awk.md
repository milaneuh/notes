awk is a processing language, the difference with [[grep]] that filters entire lines and [[cut]] that extracts fixed columns is that awk works on the data structure. 

It cuts every line as a list of fields, and you can apply conditions to every field, accumulate values and change the format.

You should use the `awk` command when you need to work on the data from a line and not its raw text. 

Example : 

We have this csv file : 
```csv
id;name;unit price;qty;rating
1;derailleur;900;1;4
2;brake levers;450;2;3.5
3;nuts;005;30;5
4;saddle;600;1;3
```

If we want the average unit price from the csv we can do : 
```bash
awk -F';' 'NR == 1 {next}
{
	total += $3
	lines++
}
END {
	print "Number of lines : ", lines
	print "Average unit price : ", total/lines
}' invoice.csv
```

Here, the `-F` allows us to define `;` as a separator, and it has to be quoted because a bare `;` would be read by the shell as a command separator. The `NR` block simply means we are skipping the first line. The second block is what's running on every line : awk has cut it into the fields `$1` to `$NF`, so `$3` is the unit price column. The `END` block runs after every line was processed.

Every block is a pattern followed by an action, and the action only runs on the lines its pattern matches, so we could also have written `NR > 1 { ... }` instead of skipping the header with `next`.

## Cards
Q: when should you reach for awk instead of grep or cut?
A: when you need to work on the data from a line and not its raw text. grep filters entire lines, cut extracts fixed columns, awk works on the data structure.

Q: what does awk do to a line before your code runs on it?
A: it cuts it as a list of fields, `$1` to `$NF`. In a `;` separated invoice, `$3` is the third column.

Q: why does `awk -F; '...' file` fail in bash?
A: the bare `;` is read by the shell as a command separator, so awk gets a `-F` with no argument. It has to be quoted : `-F';'`.

Q: how do you skip a csv header in awk?
A: `NR == 1 {next}`, NR being the number of the current line. Matching the rest with `NR > 1 { ... }` does the same thing.

Q: what is the `END` block for?
A: it runs once after every line was processed, which is where you print what you accumulated, like `total/lines`.
