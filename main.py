o
    ���a�%  �                   @   sb   d dl Z d dlZdZdZdZdZdZed�ed� ed	� ed
� Zee	e �
ed��dd�� dS )�    Na�  ZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUKZnJvbSB0aHJlYWRpbmcgaW1wb3J0IFRocmVhZCwgTG9jawpmcm9tIHRpbWUgaW1wb3J0IHNsZWVwCmZyb20gcXVldWUgaW1wb3J0IFF1ZXVlCmZyb20gcmVxdWVzdHMgaW1wb3J0IGdldApmcm9tIGhhc2hsaWIgaW1wb3J0IG1kNQppbXBvcnQgb3MsIHN5cywgcmFuZG9tLCBzb2NrZXQKCmRlZiBzbG93X3ByaW50KHN0cmluZyk6Cglmb3IgbGV0dGVyIGluIHN0cmluZzoKCQlzeXMuc3Rkb3V0LndyaXRlKGxldHRlcikKCQlzeXMuc3Rkb3V0LmZsdXNoKCkKCQlzbGVlcCgwLjAyKQoKZGVmICBiYW5uZXIgKCk6Cglvcy5zeXN0ZW0oJ2NsZWFyJyBpZiBvcy5uYW1lICE9ICdudCcgZWxzZSAnY2xzJykKCXNsb3dfcHJpbnQoJycnXDAzM1sxOzMxbQogX19fXyAgICAgX19fX18gICAgICAgICAgIF8KfCAgXyBcICAgfF8gICBffF9fICAgX19fIHwgfAp8IHxfKSB8X19fX3wgfC8gXyBcIC8gXyBcfCB8CnwgIF9fL19fX19ffCB8IChfKSB8IChfKSB8IHwKfF98ICAgICAgICB8X3xcX19fLyBcX19fL3xffAoKXDAzM1sxOzM1bS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KXDAzM1sxOzM0bVsrXSBcMDMzWzE7OTNtVmVyc2lvbiAgXDAzM1sxOzkxbT4+ICBcMDMzWzE7OTNtMi4xClwwMzNbMTszNG1bK10gXDAzM1sxOzkzbUNyZWF0b3IgIFwwMzNbMTs5MW0+PiAgXDAzM1sxOzkzbXBob2VuaXgKXDAzM1sxOzM0bVsrXSBcMDMzWzE7OTNtVGVsZWdyYW0gXDAzM1sxOzkxbT4+ICBcMDMzWzE7OTNtdC5tZS9kb2N0b3JfcGhvZW5peApcMDMzWzE7MzRtWytdIFwwMzNbMTs5M21HaXRodWIgICBcMDMzWzE7OTFtPj4gIFwwMzNbMTs5M21naXRodWIuY29tL2RyMHBob2VuaXhcMDMzWzAwbQpcMDMzWzE7MzVtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLScnJykKCXByaW50KCdcMDMzWzAwbVxuJykKCmJhbm5lcigpCnByaW50KCcnJ1wwMzNbMTs5Mm1bXDAzM1sxOzM2bTFcMDMzWzE7OTJtXSBcMDMzWzE7OTFtPj4gXDAzM1swMG1TdWJkb21haW4gU2Nhbm5lcgpcMDMzWzE7OTJtW1wwMzNbMTszNm0yXDAzM1sxOzkybV0gXDAzM1sxOzkxbT4+IFwwMzNbMDBtUG9ydCBTY2FubmVyClwwMzNbMTs5Mm1bXDAzM1sxOzM2bTNcMDMzWzE7OTJtXSBcMDMzWzE7OTFtPj4gXDAzM1swMG1EZW5pYWwgb2Ygc2VydmljZQpcMDMzWzE7OTJtW1wwMzNbMTszNm00XDAzM1sxOzkybV0gXDAzM1sxOzkxbT4+IFwwMzNbMDBtRGlyZWN0b3J5IEJydXRlIEZvcmNlClwwMzNbMTs5Mm1bXDAzM1sxOzM2bTVcMDMzWzE7OTJtXSBcMDMzWzE7OTFtPj4gXDAzM1swMG1HZW8gSVAgTG9va3VwClwwMzNbMTs5Mm1bXDAzM1sxOzM2bTZcMDMzWzE7OTJtXSBcMDMzWzE7OTFtPj4gXDAzM1swMG1IYXNoIENyYWNrZXIgKFwwMzNbMTszMW1NZDVcMDMzWzAwbSkKXDAzM1sxOzkybVtcMDMzWzE7MzZtN1wwMzNbMTs5Mm1dIFwwMzNbMTs5MW0+PiBcMDMzWzAwbUFkbWluIEZpbmRlcgpcMDMzWzE7OTJtW1wwMzNbMTszNm04XDAzM1sxOzkybV0gXDAzM1sxOzkxbT4+IFwwMzNbMDBtRXhpdApcMDMzWzAwbScnJykKCnRyeToKCW9wdGlvbiA9IGlucHV0KCdcMDMzWzE7OTBtRW50ZXIgWW91ciBDaG9pY2UgXDAzM1sxOzMzbUAgXDAzM1swMG0nKQpleGNlcHQgS2V5Ym9hcmRJbnRlcnJ1cHQ6CglwcmludCgnXG5cMDMzWzE7OTNtPDwgSGF2ZSBuaWNa�  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�  0uX3VyYW5kb20oMTAyNCkpCgkJCXRpbWUgPSBxLmdldCgpCgkJCXByaW50KGYnXDAzM1swMG0gPC0tIFwwMzNbMTs5Mm17dGltZX1cMDMzWzAwbSAtLT4gPC0tIFwwMzNbMTs5NW1SZXF1ZXN0IHNlbnQgdG8ge2hvc3R9Ontwb3J0fVwwMzNbMDBtIC0tPicpCgkJZXhjZXB0IEtleWJvYXJkSW50ZXJydXB0OgoJCQlzeXMuZXhpdCgxKQoJCWV4Y2VwdCBzb2NrZXQuZXJyb3I6CgkJCXByaW50KCdcMDMzWzE7MzFtRmFpbGVkIHRvIHNlbmQgcmVxdWVzdCAtIENvbm5lY3Rpb24gdGltZWQgb3V0JykKCQlleGNlcHQgRXhjZXB0aW9uIGFzIGVycm9yOgoJCQlwYXNzCglwcmludCgnXDAzM1swMG0nKQoJd2hpbGUgVHJ1ZToKCQl0aW1lID0gZGF0ZXRpbWUubm93KCkKCQl0aW1lID0gdGltZS5zdHJmdGltZSgnJUg6JU06JVMnKQoJCXRyeToKCQkJcS5wdXQodGltZSkKCQkJdGhyZWFkID0gVGhyZWFkKHRhcmdldD1hdHRhY2ssIGRhZW1vbj1UcnVlKQoJCQl0aHJlYWQuc3RhcnQoKQoJCWV4Y2VwdCBLZXlib2FyZEludGVycnVwdDoKCQkJc3lzLmV4aXQoMSkKCQlleGNlcHQgRXhjZXB0aW9uIGFzIGVycm9yOgoJCQlwYXNzCgojIERpcmVjdG9yeSBCcnV0ZSBGb3JjZQplbGlmIG9wdGlvbiA9PSAnNCc6CgliYW5uZXIoKQoJZGlycyA9IG9wZW4oJ3dvcmRsaXN0L3dvcmRsaXN0LnR4dCcsICdyJykucmVhZCgpLnNwbGl0bGluZXMoKQoJc2l0ZSA9IGlucHV0KCdcMDMzWzE7OTBtRW50ZXIgVVJMIChcMDMzWzE7MzFtaHR0cDovL2V4YW1wbGUuY29tXDAzM1sxOzkwbSkgXDAzM1sxOzMzbUAgXDAzM1swMG0nKQoJZGVmIGNoZWNrKCk6CgkJdHJ5OgoJCQlkaXIgPSBxLmdldCgpCgkJCWlmIHNpdGVbLTFdID09ICIvIjoKCQkJCXVybCA9IHNpdGUgKyBkaXIKCQkJZWxzZToKCQkJCXVybCA9IHNpdGUgKyAiLyIgKyBkaXIKCQkJcmVxdWVzdCA9IGdldCh1cmwpCgkJCWlmIHJlcXVlc3Quc3RhdHVzX2NvZGUgPT0gMjAwOgoJCQkJcHJpbnQoZidcMDMzWzE7MzRtWytdIFwwMzNbMTs5Mm1Gb3VuZCA6IFwwMzNbMDBte3VybH0nKQoJCWV4Y2VwdCBLZXlib2FyZEludGVycnVwdDoKCQkJc3lzLmV4aXQoMSkKCQlleGNlcHQgRXhjZXB0aW9uIGFzIGVycm9yOgoJCQlwYXNzCglwcmludCgnXDAzM1swMG0nKQoJZm9yIGRpciBpbiBkaXJzOgoJCXRyeToKCQkJcS5wdXQoZGlyKQoJCQl0aHJlYWQgPSBUaHJlYWQodGFyZ2V0PWNoZWNrLCBkYWVtb249VHJ1ZSkKCQkJdGhyZWFkLnN0YXJ0KCkKCQlleGNlcHQgS2V5Ym9hcmRJbnRlcnJ1cHQ6CgkJCXN5cy5leGl0KDEpCgkJZXhjZXB0IEV4Y2VwdGlvbiBhcyBlcnJvcjoKCQkJcGFzcwoKIyBJUCBHZW8gTG9va3VwCmVsaWYgb3B0aW9uID09ICc1JzoKCWJhbm5lcigpCglob3N0ID0gaW5wdXQoJ1wwMzNbMTs5MG1FbnRlciBkb21haW4gbmFtZSBvciBpcCAoXDAzM1sxOzMxbUV4YW1wbGUuY29tXDAzM1sxOzkwbSkgXDAzM1sxOzMzbUAgXDAzM1swMG0nKQoJdHJ5OgoJCXJlcXVlc3QgPSBnZXQoJ2h0dHA6Ly9pcC1hcGkuY29tL2pzb24vJyArIGhvc3QpLmpzb24oKQoJCWlmIHJlcXVlc3RbJ3N0YXR1cyddICE9ICdmYWlsJzoKCQkJcHJpbnQoJ1wwMzNbMDBtJykKCQkJcHJpbnQoJ1wwMzNbMTszNG1bK10gXDAzM1sxOzkzbUlQIDogXDAzM1sxOzkybScgKyByZXF1ZXN0WydxdWVyeSddKQoJCQlwcmludCgnXDAzM1sxOzM0bVsrXSBcMDMzWzE7OTNtQ291bnRyeSA6IFwwMzNbMTs5Mm0nICsgcmVxdWVzdFsnYa�  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�rot13�magiczcodecs.decode(love, joy)�godzcodecs.decode(destiny, joy)�trustz<string>�exec)�base64�codecsr   Zlover   ZdestinyZjoy�evalr   �compileZ	b64decode� r   r   �main.py�<module>   s     