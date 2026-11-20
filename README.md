![dependency graph example](doc/snap_rqt_dep.png)

## Usage

### Legend of the color in the diagram

See the snapshot above as an example. You can tell by the colors the
pkg(s):

- Red: the cursor is on.
- Blue: that you searched the dependency for.
- Green: that are directly depended upon from the "Red" pkg.

### Limitation

As of version 0.4.1, only the packages in `ROS_PACKAGE_PATH` can be
inquired on `rqt_dep`.
