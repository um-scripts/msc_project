file1 = open('TOC_REP1SJ.out.tab', 'r')
file2 = open('TOC_REP2SJ.out.tab', 'r')

f1_lines = dict()
for l1 in file1.readlines():
    c = l1.strip('\n').split('\t')
    f1_lines[tuple(c[:3])] = [c[6], c[7]]

f2_lines = dict()
for l2 in file2.readlines():
    c = l2.strip('\n').split('\t')
    f2_lines[tuple(c[:3])] = [c[6], c[7]]

file1.close()
file2.close()

c_keys = []
for f1 in f1_lines.keys():
    for f2 in f2_lines.keys():
        if f1 == f2:
            c_keys.append(f1)

commons = []
not_commons = []
for ck in c_keys:
    commons.append(list(ck) + f1_lines[ck] + f2_lines[ck])
    f1_lines.pop(ck)
    f2_lines.pop(ck)

for k, v in f1_lines.items():
    not_commons.append(['Rep1'] + list(k) + v)

for k, v in f2_lines.items():
    not_commons.append(['Rep2'] + list(k) + v)


c_file = open('TOC_Rep1Rep2_common.txt', 'w')
c_file.write('scaffold_number\tintron_start\tintron_end\ttoc_rep1_reads(u)\ttoc_rep1_reads(m)\t'
             'toc_rep2_reads(u)\ttoc_rep2_reads(m)\n')
for c in commons:
    c_file.write('\t'.join(list(c)))
    c_file.write('\n')
c_file.close()

nc_file = open('TOC_Rep1Rep2_not_common.txt', 'w')
for nc in not_commons:
    nc_file.write('\t'.join(list(nc)))
    nc_file.write('\n')
nc_file.close()
