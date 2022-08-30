


def read_PathSeq_corrected(input_file,output_file):
    list_to_store_int_tax=[]
    pathseq=open(input_file,'r')
    output=open(output_file,'w')
    n=0    

    for each_line in pathseq:
        each_line=each_line.rstrip('\n')
        if not n==0:
            each_line_list=each_line.split('\t')
            tax=each_line_list[1]
            tax_list=tax.split('|')
            unamb_reads=int(each_line_list[-2])
            
            tax_list.append(unamb_reads)
            list_to_store_int_tax.append(tax_list)
        n+=1

    print("there are ", len(list_to_store_int_tax))
    pathseq.close()
    k=0
#    q=0
    pathseq=open(input_file,'r')
    for each_line2 in pathseq:

        each_line2=each_line2.rstrip('\n')
        if not k==0:
                
            each_line_list=each_line2.split('\t')

            tax=each_line_list[1]
            tax_list=tax.split('|')

            unamb_reads=int(each_line_list[-2])

#            orig_read=unamb_reads
            if unamb_reads == 0:
                continue
            for each_clay in list_to_store_int_tax:
                if (len(tax_list) == len(each_clay[:-1])-1) and (tax_list==each_clay[:len(tax_list)]):
                    unamb_reads=unamb_reads-each_clay[-1]

            write_line=str(unamb_reads)+'\t'+'\t'.join(tax_list)
            output.write(write_line)
            output.write('\n')

        k+=1
    pathseq.close()
    return
        
input_file=[
    "/pathseq/1N.pathseq.txt.csv"
]

output_file=[
    "/krona/1N.krona"
]


for n in range(len(input_file)):
    read_PathSeq_corrected(input_file[n],output_file[n])




