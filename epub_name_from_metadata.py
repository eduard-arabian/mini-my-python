# Renames *.epub in the current directory into the 'title + 'authors + publication_date + .epub' from epub's metadata.
# pip install epub_meta
import os
import epub_meta

epub_list = [x for x in os.listdir() if x.endswith('.epub')]

for epub_file in epub_list:
    metadata = epub_meta.get_epub_metadata(epub_file)
    new_name = ''
    new_name += metadata.title + ' '
    for author in metadata.authors:
        new_name += ' ' + author
    if metadata.publication_date is not None:
        new_name += ' ' + metadata.publication_date
    new_name = new_name.replace('(', '').replace(')', '').replace('©', '').replace(':', '').replace('?', '').replace('/', '').replace('\\', '')
    new_name = (new_name[:250] + '.epub') if len(new_name) > 250 else new_name + '.epub' 
    print(new_name)
    os.rename(epub_file, new_name)
