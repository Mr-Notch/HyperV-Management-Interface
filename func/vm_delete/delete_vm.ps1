param($vmname,$vmloc)
#$vmname="python_importvm_func_1"
#$vmloc="E:\VirtualMachine\Hyper-V"
# С���������Ժ�Hyper-V��·���µ�vmname������
# ����һ��Ҫ���ö��ձ��������Ĺ�����vmname��·���µ�vmname����ֵ�Աȶԣ�
#Remove-VM -Name $vmname -Force
Remove-Item -Path "$vmloc\$vmname\*" -Recurse
Remove-Item -Path "$vmloc\$vmname" -Recurse