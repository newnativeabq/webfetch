# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 05:02:35 2018

@author: vince
"""

import re

text = "<li class='thumbwook'><a class='rel-link' href='https://images.pornpics.com/1280/201810/08/3449742/3449742_002_2c40.jpg' data-size='854x1280' data-gid='7_3449742' data-tid='1001'><img srcset='https://images.pornpics.com/300/201810/08/3449742/3449742_002_2c40.jpg 300w, https://images.pornpics.com/460/201810/08/3449742/3449742_002_2c40.jpg 460w' src='https://images.pornpics.com/300/201810/08/3449742/3449742_002_2c40.jpg' alt='Nerdy gamer girl Satin feels the call to solo masturbation during a game' sizes='(max-width: 600px) 100vw, (min-width: 600px) 1vw' width='300' height='445' /></a></li><li class='thumbwook'><a class='rel-link' href='https://images.pornpics.com/1280/201810/08/3449742/3449742_009_7311.jpg' data-size='854x1280' data-gid='7_3449742' data-tid='1001'><img srcset='https://images.pornpics.com/300/201810/08/3449742/3449742_009_7311.jpg 300w, https://images.pornpics.com/460/201810/08/3449742/3449742_009_7311.jpg 460w' src='https://images.pornpics.com/300/201810/08/3449742/3449742_009_7311.jpg' alt='Nerdy gamer girl Satin feels the call to solo masturbation during a game' sizes='(max-width: 600px) 100vw, (min-width: 600px) 1vw' width='300' height='445' /></a></li><li class='thumbwook'><a class='rel-link' href='https://images.pornpics.com/1280/201810/08/3449742/3449742_014_c764.jpg' data-size='854x1280' data-gid='7_3449742' data-tid='1001'><img srcset='https://images.pornpics.com/300/201810/08/3449742/3449742_014_c764.jpg 300w, https://images.pornpics.com/460/201810/08/3449742/3449742_014_c764.jpg 460w' src='https://images.pornpics.com/300/201810/08/3449742/3449742_014_c764.jpg' alt='Nerdy gamer girl Satin feels the call to solo masturbation during a game' sizes='(max-width: 600px) 100vw, (min-width: 600px) 1vw' width='300' height='445' /></a></li><li class='thumbwook'><a class='rel-link' href='https://images.pornpics.com/1280/201810/08/3449742/3449742_026_dfd0.jpg' data-size='854x1280' data-gid='7_3449742' data-tid='1001'><img srcset='https://images.pornpics.com/300/201810/08/3449742/3449742_026_dfd0.jpg 300w, https://images.pornpics.com/460/201810/08/3449742/3449742_026_dfd0.jpg 460w' src='https://images.pornpics.com/300/201810/08/3449742/3449742_026_dfd0.jpg' alt='Nerdy gamer girl Satin feels the call to solo masturbation during a game' sizes='(max-width: 600px) 100vw, (min-width: 600px) 1vw' width='300' height='445' /></a></li><li class='thumbwook'><a class='rel-link' href='https://images.pornpics.com/1280/201810/08/3449742/3449742_029_5db2.jpg' data-size='854x1280' data-gid='7_3449742' data-tid='1001'><img srcset='https://images.pornpics.com/300/201810/08/3449742/3449742_029_5db2.jpg 300w, https://images.pornpics.com/460/201810/08/3449742/3449742_029_5db2.jpg 460w' src='https://images.pornpics.com/300/201810/08/3449742/3449742_029_5db2.jpg' alt='Nerdy gamer girl Satin feels the call to solo masturbation during a game' sizes='(max-width: 600px) 100vw, (min-width: 600px) 1vw' width='300' height='445' /></a></li><li class='thumbwook'><a class='rel-link' href='https://images.pornpics.com/1280/201810/08/3449742/3449742_040_a7ad.jpg' data-size='1280x854' data-gid='7_3449742' data-tid='1001'><img srcset='https://images.pornpics.com/300/201810/08/3449742/3449742_040_a7ad.jpg 300w, https://images.pornpics.com/460/201810/08/3449742/3449742_040_a7ad.jpg 460w' src='https://images.pornpics.com/300/201810/08/3449742/3449742_040_a7ad.jpg' alt='Nerdy gamer girl Satin feels the call to solo masturbation during a game' sizes='(max-width: 600px) 100vw, (min-width: 600px) 1vw' width='300' height='197' /></a></li><li class='thumbwook'><a class='rel-link' href='https://images.pornpics.com/1280/201810/08/3449742/3449742_045_b632.jpg' data-size='1280x854' data-gid='7_3449742' data-tid='1001'><img srcset='https://images.pornpics.com/300/201810/08/3449742/3449742_045_b632.jpg 300w, https://images.pornpics.com/460/201810/08/3449742/3449742_045_b632.jpg 460w' src='https://images.pornpics.com/300/201810/08/3449742/3449742_045_b632.jpg' alt='Nerdy gamer girl Satin feels the call to solo masturbation during a game' sizes='(max-width: 600px) 100vw, (min-width: 600px) 1vw' width='300' height='197' /></a></li><li class='thumbwook'><a class='rel-link' href='https://images.pornpics.com/1280/201810/08/3449742/3449742_052_a8c1.jpg' data-size='854x1280' data-gid='7_3449742' data-tid='1001'><img srcset='https://images.pornpics.com/300/201810/08/3449742/3449742_052_a8c1.jpg 300w, https://images.pornpics.com/460/201810/08/3449742/3449742_052_a8c1.jpg 460w' src='https://images.pornpics.com/300/201810/08/3449742/3449742_052_a8c1.jpg' alt='Nerdy gamer girl Satin feels the call to solo masturbation during a game' sizes='(max-width: 600px) 100vw, (min-width: 600px) 1vw' width='300' height='445' /></a></li><li class='thumbwook'><a class='rel-link' href='https://images.pornpics.com/1280/201810/08/3449742/3449742_060_d2e0.jpg' data-size='854x1280' data-gid='7_3449742' data-tid='1001'><img srcset='https://images.pornpics.com/300/201810/08/3449742/3449742_060_d2e0.jpg 300w, https://images.pornpics.com/460/201810/08/3449742/3449742_060_d2e0.jpg 460w' src='https://images.pornpics.com/300/201810/08/3449742/3449742_060_d2e0.jpg' alt='Nerdy gamer girl Satin feels the call to solo masturbation during a game' sizes='(max-width: 600px) 100vw, (min-width: 600px) 1vw' width='300' height='445' /></a></li><li class='thumbwook'><a class='rel-link' href='https://images.pornpics.com/1280/201810/08/3449742/3449742_063_9b6f.jpg' data-size='854x1280' data-gid='7_3449742' data-tid='1001'><img srcset='https://images.pornpics.com/300/201810/08/3449742/3449742_063_9b6f.jpg 300w, https://images.pornpics.com/460/201810/08/3449742/3449742_063_9b6f.jpg 460w' src='https://images.pornpics.com/300/201810/08/3449742/3449742_063_9b6f.jpg' alt='Nerdy gamer girl Satin feels the call to solo masturbation during a game' sizes='(max-width: 600px) 100vw, (min-width: 600px) 1vw' width='300' height='445' /></a></li><li class='thumbwook'><a class='rel-link' href='https://images.pornpics.com/1280/201810/08/3449742/3449742_070_1af1.jpg' data-size='854x1280' data-gid='7_3449742' data-tid='1001'><img srcset='https://images.pornpics.com/300/201810/08/3449742/3449742_070_1af1.jpg 300w, https://images.pornpics.com/460/201810/08/3449742/3449742_070_1af1.jpg 460w' src='https://images.pornpics.com/300/201810/08/3449742/3449742_070_1af1.jpg' alt='Nerdy gamer girl Satin feels the call to solo masturbation during a game' sizes='(max-width: 600px) 100vw, (min-width: 600px) 1vw' width='300' height='445' /></a></li><li class='thumbwook'><a class='rel-link' href='https://images.pornpics.com/1280/201810/08/3449742/3449742_081_2dfb.jpg' data-size='854x1280' data-gid='7_3449742' data-tid='1001'><img srcset='https://images.pornpics.com/300/201810/08/3449742/3449742_081_2dfb.jpg 300w, https://images.pornpics.com/460/201810/08/3449742/3449742_081_2dfb.jpg 460w' src='https://images.pornpics.com/300/201810/08/3449742/3449742_081_2dfb.jpg' alt='Nerdy gamer girl Satin feels the call to solo masturbation during a game' sizes='(max-width: 600px) 100vw, (min-width: 600px) 1vw' width='300' height='445' /></a></li><li class='thumbwook'><a class='rel-link' href='https://images.pornpics.com/1280/201810/08/3449742/3449742_082_781e.jpg' data-size='854x1280' data-gid='7_3449742' data-tid='1001'><img srcset='https://images.pornpics.com/300/201810/08/3449742/3449742_082_781e.jpg 300w, https://images.pornpics.com/460/201810/08/3449742/3449742_082_781e.jpg 460w' src='https://images.pornpics.com/300/201810/08/3449742/3449742_082_781e.jpg' alt='Nerdy gamer girl Satin feels the call to solo masturbation during a game' sizes='(max-width: 600px) 100vw, (min-width: 600px) 1vw' width='300' height='445' /></a></li><li class='thumbwook'><a class='rel-link' href='https://images.pornpics.com/1280/201810/08/3449742/3449742_095_03d3.jpg' data-size='854x1280' data-gid='7_3449742' data-tid='1001'><img srcset='https://images.pornpics.com/300/201810/08/3449742/3449742_095_03d3.jpg 300w, https://images.pornpics.com/460/201810/08/3449742/3449742_095_03d3.jpg 460w' src='https://images.pornpics.com/300/201810/08/3449742/3449742_095_03d3.jpg' alt='Nerdy gamer girl Satin feels the call to solo masturbation during a game' sizes='(max-width: 600px) 100vw, (min-width: 600px) 1vw' width='300' height='445' /></a></li><li class='thumbwook'><a class='rel-link' href='https://images.pornpics.com/1280/201810/08/3449742/3449742_100_4032.jpg' data-size='854x1280' data-gid='7_3449742' data-tid='1001'><img srcset='https://images.pornpics.com/300/201810/08/3449742/3449742_100_4032.jpg 300w, https://images.pornpics.com/460/201810/08/3449742/3449742_100_4032.jpg 460w' src='https://images.pornpics.com/300/201810/08/3449742/3449742_100_4032.jpg' alt='Nerdy gamer girl Satin feels the call to solo masturbation during a game' sizes='(max-width: 600px) 100vw, (min-width: 600px) 1vw' width='300' height='445' /></a></li><li class='thumbwook'><a class='rel-link' href='https://images.pornpics.com/1280/201810/08/3449742/3449742_109_15c0.jpg' data-size='1280x854' data-gid='7_3449742' data-tid='1001'><img srcset='https://images.pornpics.com/300/201810/08/3449742/3449742_109_15c0.jpg 300w, https://images.pornpics.com/460/201810/08/3449742/3449742_109_15c0.jpg 460w' src='https://images.pornpics.com/300/201810/08/3449742/3449742_109_15c0.jpg' alt='Nerdy gamer girl Satin feels the call to solo masturbation during a game' sizes='(max-width: 600px) 100vw, (min-width: 600px) 1vw' width='300' height='197' /></a></li>"


linklist = []

for group in text.split(' '):
    if 'href' in group:
        linklist.append(group)

print(linklist)

search = linklist[0].split("'")
print(search)