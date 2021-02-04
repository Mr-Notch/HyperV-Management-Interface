def guiwriter():
    print('-------------')
    print('| Import-VM |')
    print('-------------')
    print('')
    template_name = input('Template Name (String) : ')
    vm_name = input('VM Name (String) : ')
    vm_cpunum = int(input('CPU Number (Int64) : '))
    vm_ramsize = int(input('RAM Size (Int64) : '))
    maturity_time = input('Maturity TIme (String Date) : ')
    if template_name == vm_name:
        print('Error: VM Name cannot be the same as Template Name')
        return False