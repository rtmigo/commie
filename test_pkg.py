from chkpkg import Package

if __name__ == "__main__":
    with Package() as pkg:
        pkg.run_python_code('from commie import iter_comments_go')

    print("\nPackage is OK!")

