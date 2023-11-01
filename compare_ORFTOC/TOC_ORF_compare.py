file1 = open('ORF_Rep1Rep2_common.txt', 'r')
file2 = open('TOC_Rep1Rep2_common.txt', 'r')

head1 = file1.readline().strip('\n').split('\t')
head2 = file2.readline().strip('\n').split('\t')
assert tuple(head1[:3]) == tuple(head2[:3])
head = head1 + head2[3:]

f1_lines = dict()
for l1 in file1.readlines():
    c = l1.strip('\n').split('\t')
    f1_lines[tuple(c[:3])] = c[3:]

f2_lines = dict()
for l2 in file2.readlines():
    c = l2.strip('\n').split('\t')
    f2_lines[tuple(c[:3])] = c[3:]

file1.close()
file2.close()

c_keys = []
for f1 in f1_lines.keys():
    for f2 in f2_lines.keys():
        if f1 == f2:
            c_keys.append(f1)

commons = []
for ck in c_keys:
    commons.append(list(ck) + f1_lines[ck] + f2_lines[ck])
    f1_lines.pop(ck)
    f2_lines.pop(ck)

c_file = open('TOC_ORF_common.txt', 'w')
c_file.write('\t'.join(head) + '\n')
for c in commons:
    c_file.write('\t'.join(list(c)))
    c_file.write('\n')
c_file.close()

file = open('ORF_not_common.txt', 'w')
file.write('\t'.join(head1) + '\n')
for k, v in f1_lines.items():
    file.write('\t'.join(list(k) + v) + '\n')
file.close()

file = open('TOC_not_common.txt', 'w')
file.write('\t'.join(head2) + '\n')
for k, v in f2_lines.items():
    file.write('\t'.join(list(k) + v) + '\n')
file.close()
