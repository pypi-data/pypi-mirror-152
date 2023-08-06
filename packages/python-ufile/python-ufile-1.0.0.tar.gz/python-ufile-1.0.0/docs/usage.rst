=====
Usage
=====

To use python-ufile to upload a file::

    from python_ufile import Ufile
    ufile = Ufile()
    link = ufile.upload_file("file_name.mp4")
    print(link)

To use python-ufile to get a temporary link to download a file (it needs API key)::

    from python_ufile import Ufile
    ufile = Ufile("API_KEY")
    link = ufile.download_file_link("SLUG")
    print(link)

To use python-ufile to download a file (it needs API key)::

    from python_ufile import Ufile
    ufile = Ufile("API_KEY")
    ufile.download_file("SLUG", "output.mp4")

