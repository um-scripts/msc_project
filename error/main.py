input_file = 'seq_error_orf_input.csv'
search_files = ['ORF1Rep1SJ.out.tab', 'ORF1Rep2SJ.out.tab', 'TOC_Rep1SJ.out.tab', 'TOC_Rep2SJ.out.tab']
output_file = 'out.tab'

inp_f = open(input_file, 'r')
f = [open(ff, 'r') for ff in search_files]
out_f = open(output_file, 'w')
h = inp_f.readline().strip('\n').split(',') + search_files
out_f.write('\t'.join(h) + '\n')
for i, line in enumerate(inp_f.readlines()):
    c = line.strip('\n').split(',')
    cr = []
    for file in f:
        r = []
        for fl in file.readlines():
            cl = fl.strip('\n').split('\t')
            if cl[0] == c[0] and int(cl[1]) == int(c[1]) and int(cl[2]) == int(c[2]):
                r.append(cl[6])
        file.seek(0)
        if len(r) > 1:
            print('Multiple occurrence of line ' + str(i+1) + ': ' + line.strip('\n'), 'in file ' + file.name)
            cr.append('?')
        elif len(r) == 0:
            cr.append('-')
        else:
            cr.append(r[0])

    out_f.write('\t'.join(c + cr) + '\n')

out_f.close()
inp_f.close()
for file in f:
    file.close()