from chkpkg import Package

if __name__ == "__main__":
    with Package() as pkg:
        pkg.run_python_code('import xpnt')
        pkg.run_shell_code('xpnt')

    print("\nPackage is OK!")

