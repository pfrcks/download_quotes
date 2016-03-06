quotes = open('quotes1', 'r').readlines()
final = open('final_quotes', 'w')

for i, lines in enumerate(quotes):
    if lines == '\n':
        continue
    if i == 0 or i == (len(quotes)-1):
        final.write(lines)
        continue
    if quotes[i][0]!='\t' and quotes[i+1][0]=='\t':
        final.write('%\n')
        final.write(lines)
    else:
        if lines[0] == '\t':
            final.write('\t'+str(lines))
        else:
            final.write('\t\t'+str(lines))
