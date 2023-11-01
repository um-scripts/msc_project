f1 = open('intron.txt', 'r')
f2 = open('NoRepetition_SJout_ALL.txt', 'r')

head1 = f1.readline().strip('\n').split('\t')
head2 = f2.readline().strip('\n').split('\t')
list1 = [tuple(line.strip('\n').split('\t')[i] for i in [0, 1, 6, 7]) for line in f1.readlines()]
list2 = [tuple(line.strip('\n').split('\t')) for line in f2.readlines()]

not_an_count = 0
out = open(f2.name.strip('.txt') + '_annotation.txt', 'w')
out.write('scaffold_number\tgene_id\tintron_start\tintron_end\t' + '\t'.join(head2[3:]) + '\tannotated\tnovel\n')
for l2 in list2:
    f = False
    for l1 in list1:
        if l1[0] == l2[0] and l1[2] == l2[1] and l1[3] == l2[2]:
            out.write('\t'.join(list(l1) + list(l2[3:]) + ['Yes', 'No']))
            f = True
            break
    if not f:
        out.write('\t'.join([l2[0], 'NA'] + list(l2[1:]) + ['No', 'Yes']))
        not_an_count += 1
    out.write('\n')

out.close()
print(not_an_count)
