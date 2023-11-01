# Headers in output file
# scaffold_number
# gene_id
# rna_id
# rna_type
# rna_start
# rna_end
# intron_start
# intron_end
# +/-


def detect_introns(rna):
    p_start = rna['self']['start']
    p_end = rna['self']['end']

    introns = []
    for exon in sorted(rna['exons'], key=lambda e: e['start']):
        assert exon['start'] >= p_start and exon['end'] <= p_end
        if exon['start'] != p_start:
            introns[-1]['end'] = exon['start'] - 1
        if exon['end'] != p_end:
            introns.append({'start': exon['end'] + 1})

    return introns


source = open('AmoebaDB-56_EhistolyticaHM1IMSS.gff')
data = {}
for line in source.readlines():
    if not line.startswith('##'):
        comps = line.rstrip('\n').split('\t')
        assert len(comps) == 9

        part = {}
        for c in comps[8].split(';'):
            cs = c.partition('=')
            part[cs[0]] = cs[2]

        assert 'ID' in part
        data[part['ID']] = {
            'name': comps[2],
            'scaffold_no': comps[0],
            'start': int(comps[3]),
            'end': int(comps[4]),
            '+/-': comps[6],
            'info': part
        }


rna_data = {}
for k in data.keys():
    if data[k]['name'] == 'exon':
        assert 'Parent' in data[k]['info']
        parent = data[k]['info']['Parent']
        if parent not in rna_data:
            rna_data[parent] = {
                'self': data[parent],
                'exons': []
            }

        rna_data[parent]['exons'].append(data[k])


output_file = open('intron.txt', 'w')
unique_gene_with_introns = 0
intron_count = 0
output_file.write('scaffold_number\tgene_id\trna_id\trna_type\trna_start\trna_end\tintron_start\tintron_end\t+/-\n')
for rna_id, RNA in rna_data.items():
    scaffold_number = RNA['self']['scaffold_no']
    gene_id = RNA['self']['info']['Parent']
    name = RNA['self']['name']
    rna_start = RNA['self']['start']
    rna_end = RNA['self']['end']
    pn_type = RNA['self']['+/-']
    introns = detect_introns(RNA)
    intron_count += len(introns)
    if len(introns) >= 1:
        unique_gene_with_introns += 1
    for intron in introns:
        line = scaffold_number + '\t' \
            + gene_id + '\t'\
            + rna_id + '\t'\
            + name + '\t'\
            + str(rna_start) + '\t'\
            + str(rna_end) + '\t'\
            + str(intron['start']) + '\t'\
            + str(intron['end']) + '\t' \
            + pn_type + '\n'
        output_file.write(line)

output_file.close()
print('Total number of Intron count: ', intron_count)
print('Unique Genes with Introns: ', unique_gene_with_introns)
