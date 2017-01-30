# Quit Merge

Add these lines to your `~/.gitconfig`

    [merge "quitmerge"]
    name = Quit – Quads in Git – merge driver
    driver = quit-merge %O %A %B

and these lines to a `.gitattributes` file in a git repository:

    *.nt    merge=quitmerge
    *.nq    merge=quitmerge

# License

Copyright (C) 2017 Natanael Arndt <http://aksw.org/NatanaelArndt>

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, see <http://www.gnu.org/licenses>.
Please see [LICENSE](LICENSE) for further information.
