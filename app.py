"""Hops flask middleware example"""
from flask import Flask
import ghhops_server as hs
import rhino3dm


# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)


# flask app can be used for other stuff drectly
@app.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"

# hs.HopsNumber(name="Angle", nickname="Ang", description="Angle"),
# hs.HopsInteger(name="Grid", nickname="G", description="Grid size"),
# hs.HopsBoolean(name="Adaptive", nickname="Ad", description="Adaptive meshing"),
# hs.HopsString(name="String", nickname="S", description="String to mesh"),

# hs.HopsVector(name="Vector", nickname="V", description="Vector to mesh")
# hs.HopsPoint(name="Point", nickname="P", description="Point to mesh"),
# hs.HopsLine(name="Line", nickname="L", description="Line to mesh"),
# hs.HopsCurve(name="Curve", nickname="C", description="Curve to mesh"),

# hs.HopsSurface(name="Surface", nickname="S", description="Surface to mesh"),
# hs.HopsBrep(name="Brep", nickname="B", description="Brep to mesh"),
# hs.HopsMesh(name="Mesh", nickname="M", description="Mesh to mesh"),
# hs.HopsSubD(name="SubD", nickname="SD", description="SubD to mesh"),

# hs.HopsParamAccess(name="Param", nickname="Pa", description="Parametric access"),
# hs.HopsDefault(name="Density", nickname="D", description="Density"),
# hs.HopsFlask(name="Flask", nickname="F", description="Flask to mesh"),
# hs._HopsEncoder(name="Encoder", nickname="En", description="Encoder to mesh")



@hops.component(
    "/pointat",
    name="PointAt",
    nickname="PtAt",
    description="Get point along curve",
    icon="pointat.png",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on Curve to evaluate")
    ],
    outputs=[hs.HopsPoint("P", "P", "Point on curve at t")]
)
def pointat(curve: rhino3dm.Curve, t=0.0):
    return curve.PointAt(t)


@hops.component(
    "/srf4pt",
    name="4Point Surface",
    nickname="Srf4Pt",
    description="Create ruled surface from four points",
    inputs=[
        hs.HopsPoint("Corner A", "A", "First corner"),
        hs.HopsPoint("Corner B", "B", "Second corner"),
        hs.HopsPoint("Corner C", "C", "Third corner"),
        hs.HopsPoint("Corner D", "D", "Fourth corner")
    ],
    outputs=[hs.HopsSurface("Surface", "S", "Resulting surface")]
)
def ruled_surface(a: rhino3dm.Point3d,
                  b: rhino3dm.Point3d,
                  c: rhino3dm.Point3d,
                  d: rhino3dm.Point3d):
    edge1 = rhino3dm.LineCurve(a, b)
    edge2 = rhino3dm.LineCurve(c, d)
    return rhino3dm.NurbsSurface.CreateRuledSurface(edge1, edge2)

# param containers in grasshopper 
# are represented as lists in python
@hops.component(
    "/createpoint",
    name="Create Point",
    nickname="Pt",
    description="Create point",
    inputs=[
        hs.HopsNumber("X", "X", "X coordinate of point"),
        hs.HopsNumber("Y", "Y", "Y coordinate of point"),
        hs.HopsNumber("Z", "Z", "Z coordinate of point")
    ],
    outputs=[hs.HopsPoint("Point", "P", "Resulting point")]
)
def create_point(x=0.0, y=0.0, z=0.0):
    return rhino3dm.Point3d(x, y, z)


@hops.component(
    "/createCurve",
    name="Create Curve",
    nickname="Crv",
    description="Create curve",
    inputs=[
        hs.HopsPoint("Start", "S", "Start point of curve"),
        hs.HopsPoint("End", "E", "End point of curve")
    ],
    outputs=[hs.HopsCurve("Curve", "C", "Resulting curve")]
)
def create_curve(start: rhino3dm.Point3d, end: rhino3dm.Point3d):
    return rhino3dm.LineCurve(start, end)  

@hops.component(
    "/createSurface",
    name="Create Surface",
    nickname="Srf",
    description="Create surface",
    inputs=[
        hs.HopsPoint("Corner A", "A", "First corner"),
        hs.HopsPoint("Corner B", "B", "Second corner"),
        hs.HopsPoint("Corner C", "C", "Third corner"),
        hs.HopsPoint("Corner D", "D", "Fourth corner")
    ],
    outputs=[hs.HopsSurface("Surface", "S", "Resulting surface")]
)
def create_surface(a: rhino3dm.Point3d,
                     b: rhino3dm.Point3d,
                     c: rhino3dm.Point3d,
                     d: rhino3dm.Point3d):
     edge1 = rhino3dm.LineCurve(a, b)
     edge2 = rhino3dm.LineCurve(c, d)
     return rhino3dm.NurbsSurface.CreateRuledSurface(edge1, edge2)

@hops.component(
    "/createBrep",
    name="Create Brep",
    nickname="Brep",
    description="Create brep",
    inputs=[
        hs.HopsSurface("Surface", "S", "Surface to create brep from")
    ],
    outputs=[hs.HopsBrep("Brep", "B", "Resulting brep")]
)
def create_brep(surface: rhino3dm.NurbsSurface):
    return rhino3dm.Brep.CreateFromSurface(surface)


# create hops line
@hops.component(
    "/createLine",
    name="Create Line",
    nickname="Ln",
    description="Create line",
    inputs=[
        hs.HopsPoint("Start", "S", "Start point of line"),
        hs.HopsPoint("End", "E", "End point of line")
    ],
    outputs=[hs.HopsLine("Line", "L", "Resulting line")]
)
def create_line(start: rhino3dm.Point3d, end: rhino3dm.Point3d):
    return rhino3dm.LineCurve(start, end)



# create hops vector
@hops.component(
    "/createVector",
    name="Create Vector",
    nickname="Vec",
    description="Create vector",
    inputs=[
        hs.HopsNumber("X", "X", "X coordinate of vector"),
        hs.HopsNumber("Y", "Y", "Y coordinate of vector"),
        hs.HopsNumber("Z", "Z", "Z coordinate of vector")
    ],
    outputs=[hs.HopsVector("Vector", "V", "Resulting vector")]
)
def create_vector(x: float, y: float, z: float):
    return rhino3dm.Vector3d(x, y, z)

# create hops mesh
# create hops subd

"""
 ██████╗██╗   ██╗██████╗ ██╗   ██╗███████╗███████╗
██╔════╝██║   ██║██╔══██╗██║   ██║██╔════╝██╔════╝
██║     ██║   ██║██████╔╝██║   ██║█████╗  ███████╗
██║     ██║   ██║██╔══██╗╚██╗ ██╔╝██╔══╝  ╚════██║
╚██████╗╚██████╔╝██║  ██║ ╚████╔╝ ███████╗███████║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚══════╝
                                                  
"""

"""curve domain
Domain
rhino3dm.Interval: Gets or sets the domain of the curve.
"""
@hops.component(
    "/crvDomainT0T1",
    name="Curve Domain",
    nickname="CrvDom",
    description="Curve domain",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to get domain from")
    ],
    outputs=[hs.HopsNumber("T0", "T0", "T0 of domain"), hs.HopsNumber("T1", "T1", "T1 of domain")]
)
def crv_domain(curve: rhino3dm.Curve):
    return curve.Domain.T0, curve.Domain.T1

"""
curve dimension
Dimension
int: Gets the dimension of the object. 
The dimension is typically three. 
For parameter space trimming curves the dimension is two. 
In rare cases the dimension can be one or greater than three.
"""
@hops.component(
    "/crvDimension",
    name="Curve Dimension",
    nickname="CrvDim",
    description="Curve dimension",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to get dimension from")
    ],
    outputs=[hs.HopsNumber("Dimension", "D", "Dimension of curve")]
)
def crv_dimension(curve: rhino3dm.Curve):
    return curve.Dimension

"""
curve span count
SpanCount
int: Gets the number of non-empty smooth (c-infinity) spans in the curve.
"""
@hops.component(
    "/crvSpanCount",
    name="Curve Span Count",
    nickname="CrvSpan",
    description="Curve span count",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to get span count from")
    ],
    outputs=[hs.HopsNumber("SpanCount", "Span", "Span count of curve")]
)
def crv_span_count(curve: rhino3dm.Curve):
    return curve.SpanCount

"""
curve degree
Degree
int: Gets the maximum algebraic degree 
of any span or a good estimate if 
curve spans are not algebraic.
"""
@hops.component(
    "/crvDegree",
    name="Curve Degree",
    nickname="CrvDeg",
    description="Curve degree",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to get degree from")
    ],
    outputs=[hs.HopsNumber("Degree", "Deg", "Degree of curve")]
)
def crv_degree(curve: rhino3dm.Curve):
    return curve.Degree

"""
curve IsClosed
IsClosed
bool: Gets a value indicating whether 
or not this curve is a closed curve.
"""
@hops.component(
    "/crvIsClosed",
    name="Curve Is Closed",
    nickname="CrvClosed",
    description="Curve is closed",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to get is closed from")
    ],
    outputs=[hs.HopsBoolean("IsClosed", "Closed", "Is curve closed")]
)
def crv_is_closed(curve: rhino3dm.Curve):
    return curve.IsClosed

"""
curve IsPeriodic
IsPeriodic
bool: Gets a value indicating whether 
or not this curve is considered to be Periodic.
"""
@hops.component(
    "/crvIsPeriodic",
    name="Curve Is Periodic",
    nickname="CrvPeriodic",
    description="Curve is periodic",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to get is periodic from")
    ],
    outputs=[hs.HopsBoolean("IsPeriodic", "Periodic", "Is curve periodic")]
)
def crv_is_periodic(curve: rhino3dm.Curve):
    return curve.IsPeriodic

"""
curve PointAtStart
PointAtStart
rhino3dm.Point3d: 
Evaluates point at the start of the curve.
"""
@hops.component(
    "/crvPointAtStart",
    name="Curve Point At Start",
    nickname="CrvStart",
    description="Curve point at start",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to get point at start from")
    ],
    outputs=[hs.HopsPoint("PointAtStart", "P", "Point at start of curve")]
)
def crv_point_at_start(curve: rhino3dm.Curve):
    return curve.PointAtStart

"""
curve PointAtEnd
PointAtEnd
rhino3dm.Point3d:
Evaluates point at the end of the curve.
"""
@hops.component(
    "/crvPointAtEnd",
    name="Curve Point At End",
    nickname="CrvEnd",
    description="Curve point at end",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to get point at end from")
    ],
    outputs=[hs.HopsPoint("PointAtEnd", "P", "Point at end of curve")]
)
def crv_point_at_end(curve: rhino3dm.Curve):
    return curve.PointAtEnd

"""
curve TangentAtStart
TangentAtStart
rhino3dm.Vector3d: Evaluates the unit 
tangent vector at the start of the curve.
"""
@hops.component(
    "/crvTangentAtStart",
    name="Curve Tangent At Start",
    nickname="CrvStartTang",
    description="Curve tangent at start", 
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to get tangent at start from")
    ],
    outputs=[hs.HopsVector("TangentAtStart", "T", "Tangent at start of curve")]
)   
def crv_tangent_at_start(curve: rhino3dm.Curve):
    return curve.TangentAtStart

"""
curve TangentAtEnd
TangentAtEnd
rhino3dm.Vector3d: Evaluates the unit
tangent vector at the end of the curve.
"""
@hops.component(
    "/crvTangentAtEnd",
    name="Curve Tangent At End",
    nickname="CrvEndTang",
    description="Curve tangent at end",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to get tangent at end from")
    ],
    outputs=[hs.HopsVector("TangentAtEnd", "T", "Tangent at end of curve")]
)   
def crv_tangent_at_end(curve: rhino3dm.Curve):
    return curve.TangentAtEnd

"""
static Create Control Point Curve
staticCreateControlPointCurve(points, degree)
Constructs a curve from a set of control-point locations.

Parameters:	
points (list[rhino3dm.Point3d]) – Control points.
degree (int) – Degree of curve. The number of control points must be at least degree+1.
Return type:	
rhino3dm.Curve
"""
@hops.component(
    "/crvCP5",
    name="Create Control Point Curve",
    nickname="CrvCreateCP",
    description="Create control point curve",
    inputs=[
        hs.HopsPoint("Points", "P", "Control points", access=hs.HopsParamAccess.LIST),
        hs.HopsInteger("Degree", "D", "Degree of curve")
    ],
    outputs=[hs.HopsCurve("Curve", "C", "Curve")]
)
def crvCP5(points, degree):
    return rhino3dm.Curve.CreateControlPointCurve(points, degree)

"""
curve Change Dimension
ChangeDimension(desiredDimension)
Changes the dimension of a curve.

Parameters:	desiredDimension (int) – The desired dimension.
Returns:	True if the curve’s dimension was already desired
Dimension or if the curve’s dimension was successfully 
changed to desiredDimension; otherwise false.
Return type:	bool
"""
@hops.component(
    "/crvChangeDimension",
    name="Change Dimension",
    nickname="CrvChangeDim",
    description="Change dimension of curve",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to change dimension of"),
        hs.HopsInteger("DesiredDimension", "D", "Desired dimension")
    ],
    outputs=[hs.HopsBoolean("Changed", "Ch", "Changed")]
)
def crv_change_dimension(curve: rhino3dm.Curve, desiredDimension):
    return curve.ChangeDimension(desiredDimension)

"""
curve IsLinear
IsLinear(tolerance)
Test a curve to see if it is linear 
to within RhinoMath.ZeroTolerance units (1e-12).

Returns:	True if the curve is linear.
Return type:	bool
"""
@hops.component(
    "/crvIsLinear",
    name="Is Linear",
    nickname="CrvLinear",
    description="Curve is linear",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to test")
    ],
    outputs=[hs.HopsBoolean("IsLinear", "Lin", "Is linear")]
)
def crv_is_linear(curve: rhino3dm.Curve):
    return curve.IsLinear()

"""
curve is polyline
IsPolyline()
Several types of Curve can have the form of a polyline including a degree 1 NurbsCurve, a PolylineCurve, and a PolyCurve all of whose segments are some form of polyline. IsPolyline tests a curve to see if it can be represented as a polyline.

Returns:	True if this curve can be represented as a polyline; otherwise, false.
Return type:	bool
"""
@hops.component(
    "/crvIsPolyline",
    name="Is Polyline",
    nickname="CrvPolyline",
    description="Curve is polyline",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to test")
    ],
    outputs=[hs.HopsBoolean("IsPolyline", "Poly", "Is polyline")]
)
def crv_is_polyline(curve: rhino3dm.Curve):
    return curve.IsPolyline()

"""curve try get polyline
TryGetPolyline()
Several types of Curve can have the form of a 
polyline including a degree 1 NurbsCurve, 
a PolylineCurve, and a PolyCurve all of 
whose segments are some form of polyline. 
IsPolyline tests a curve to see if it can be represented as a polyline.

Returns:	tuple (bool, rhino3dm.Polyline)
True if this curve can be represented as a polyline; otherwise, false.
If True is returned, then the polyline form is returned here.
Return type:	(bool, rhino3dm.Polyline)
"""
# @hops.component(
#     "/crvTryGetPolyline",
#     name="Try Get Polyline",
#     nickname="CrvTryPoly",
#     description="Try get polyline",
#     inputs=[
#         hs.HopsCurve("Curve", "C", "Curve to test")
#     ],
#     outputs=[hs.HopsLine("Polyline", "Poly", "Polyline")]
# )
# def crv_try_get_polyline(curve: rhino3dm.Curve):
#     polyline = rhino3dm.Polyline()
#     if curve.TryGetPolyline(polyline):
#         return polyline
#     else:
#         return None


"""
curve is arc
IsArc(tolerance)
Test a curve to see if it can be represented 
by an arc or circle within RhinoMath.ZeroTolerance.

Returns:	True if the curve can 
be represented by an arc or a circle within tolerance.
Return type:	bool
"""
@hops.component(
    "/crvIsArc",
    name="Is Arc",
    nickname="CrvArc",
    description="Curve is arc",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to test")
    ],
    outputs=[hs.HopsBoolean("IsArc", "Arc", "Is arc")]
)
def crv_is_arc(curve: rhino3dm.Curve):
    return curve.IsArc()

# curve try get arc

"""
curve is circle
IsCircle(tolerance)
Test a curve to see if it can be represented 
by a circle within RhinoMath.ZeroTolerance.

Returns:	True if the Curve can be 
represented by a circle within tolerance.
Return type:	bool
"""
@hops.component(
    "/crvIsCircle",
    name="Is Circle",
    nickname="CrvCircle",
    description="Curve is circle",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to test")
    ],
    outputs=[hs.HopsBoolean("IsCircle", "Circ", "Is circle")]
)
def crv_is_circle(curve: rhino3dm.Curve):
    return curve.IsCircle()

# curve try get circle

"""
curve is ellipse
IsEllipse(tolerance)
Test a curve to see if it can be represented 
by an ellipse within RhinoMath.ZeroTolerance.

Returns:	True if the Curve can be 
represented by an ellipse within tolerance.
Return type:	bool
"""
@hops.component(
    "/crvIsEllipse",
    name="Is Ellipse",
    nickname="CrvEllipse",
    description="Curve is ellipse",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to test")
    ],
    outputs=[hs.HopsBoolean("IsEllipse", "Ell", "Is ellipse")]
)
def crv_is_ellipse(curve: rhino3dm.Curve):
    return curve.IsEllipse()

# curve try get ellipse

"""
curve is planar
IsPlanar(tolerance)
Test a curve for planarity.

Returns:	True if the curve is planar (flat) 
to within RhinoMath.ZeroTolerance units (1e-12).
Return type:	bool
"""
@hops.component(
    "/crvIsPlanar",
    name="Is Planar",
    nickname="CrvPlanar",
    description="Curve is planar",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to test")
    ],
    outputs=[hs.HopsBoolean("IsPlanar", "Plan", "Is planar")]
)
def crv_is_planar(curve: rhino3dm.Curve):
    return curve.IsPlanar()

"""
curve change closed seam
ChangeClosedCurveSeam(t)
If this curve is closed, then modify it 
so that the start/end point is at 
curve parameter t.

Parameters:	t (float) – Curve parameter 
of new start/end point. The returned 
curves domain will start at t.
Returns:	True on success, False on failure.
Return type:	bool
"""
@hops.component(
    "/crvChangeClosedCurveSeam",
    name="Change Closed Curve Seam",
    nickname="CrvChangeClosedCurveSeam",
    description="Change closed curve seam",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to change seam of"),
        hs.HopsNumber("Parameter", "T", "Parameter of new start/end point")
    ],
    outputs=[hs.HopsBoolean("Changed", "Ch", "Changed")]
)
def crv_change_closed_curve_seam(curve: rhino3dm.Curve, parameter):
    return curve.ChangeClosedCurveSeam(parameter)

"""
curve is closable
IsClosable(tolerance, minimumAbsoluteSize, 
minimumRelativeSize)
Decide if it makes sense to close off 
this curve by moving the endpoint to the 
start based on start-end gap size and 
length of curve as approximated by 
chord defined by 6 points.

Returns:	True if start and end points 
are close enough based on above conditions.
Return type:	bool
"""
@hops.component(
    "/crvIsClose",
    name="Is Closable",
    nickname="CrvClosable",
    description="Curve is closable",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to test"),
        hs.HopsNumber("Tolerance", "T", "Tolerance"),
        hs.HopsNumber("MinimumAbsoluteSize", "MA", "Minimum absolute size"),
        hs.HopsNumber("MinimumRelativeSize", "MR", "Minimum relative size")
    ],
    outputs=[hs.HopsBoolean("IsClosable", "Clos", "Is closable")]
)
def crv_is_close(curve: rhino3dm.Curve, tolerance, minimum_absolute_size, minimum_relative_size):
    return curve.IsClosable(tolerance, minimum_absolute_size, minimum_relative_size)

"""
curve reverse
Reverse()
Reverses the direction of the curve.

Returns:	True on success, False on failure.
Return type:	bool
"""
@hops.component(
    "/crvReverse",
    name="Reverse",
    nickname="CrvReverse",
    description="Curve reverse",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to reverse")
    ],
    outputs=[hs.HopsBoolean("Reversed", "Rev", "Reversed")]
)
def crv_reverse(curve: rhino3dm.Curve):
    return curve.Reverse()

"""
curve close curve orientation
ClosedCurveOrientation()
Determines the orientation (counterclockwise or clockwise) 
of a closed, planar curve in the world XY plane. 
Only works with simple (no self intersections) closed, planar curves.

Returns:	The orientation of this curve with respect to world XY plane.
Return type:	CurveOrientation
"""
@hops.component(
    "/crvClosedCurveOrientation",
    name="Closed Curve Orientation",
    nickname="CrvClosedCurveOrientation",
    description="Curve close curve orientation",
    inputs=[    
        hs.HopsCurve("Curve", "C", "Curve to test")
    ],
    # bugging out with hs.HopsEnum
    outputs=[hs.HopsInteger("Orientation", "O", "Orientation", ["Clockwise", "Counterclockwise"])]
)
def crv_closed_curve_orientation(curve: rhino3dm.Curve):
    return curve.ClosedCurveOrientation()

"""
curve point at parameter
PointAt(t)
Evaluates point at a curve parameter.

Parameters:	t (float) – Evaluation parameter.
Returns:	Point (location of curve at the parameter t).
Return type:	rhino3dm.Point3d
"""
@hops.component(
    "/crvPointAt",
    name="Point At",
    nickname="CrvPointAt",
    description="Curve point at parameter",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("Parameter", "T", "Parameter to evaluate")
    ],
    outputs=[hs.HopsPoint("Point", "P", "Point")]
)
def crv_point_at(curve: rhino3dm.Curve, parameter):
    return curve.PointAt(parameter)

"""
curve set start point
SetStartPoint(point)
Forces the curve to start at a specified point. Not all curve types support this operation.

Parameters:	point (rhino3dm.Point3d) – New start point of curve.
Returns:	True on success, False on failure.
Return type:	bool
"""
@hops.component(
    "/crvSetStartPoint",
    name="Set Start Point",
    nickname="CrvSetStartPoint",
    description="Curve set start point",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to set start point of"),
        hs.HopsPoint("Point", "P", "Point to set start point of")
    ],
    outputs=[hs.HopsBoolean("Set", "Set", "Set")]
)
def crv_set_start_point(curve: rhino3dm.Curve, point: rhino3dm.Point3d):
    return curve.SetStartPoint(point)

"""
curve set end point
SetEndPoint(point)
Forces the curve to end at a specified point. Not all curve types support this operation.

Parameters:	point (rhino3dm.Point3d) – New end point of curve.
Returns:	True on success, False on failure.
Return type:	bool
"""
@hops.component(
    "/crvSetEndPoint",
    name="Set End Point",
    nickname="CrvSetEndPoint",
    description="Curve set end point",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to set end point of"),
        hs.HopsPoint("Point", "P", "Point to set end point of")
    ],
    outputs=[hs.HopsBoolean("Set", "Set", "Set")]
)
def crv_set_end_point(curve: rhino3dm.Curve, point: rhino3dm.Point3d):
    return curve.SetEndPoint(point)

""".
TangentAt(t)
Evaluates the unit tangent vector at a curve parameter.

Parameters:	t (float) – Evaluation parameter.
Returns:	Unit tangent vector of the curve at the parameter t.
Return type:	rhino3dm.Vector3d
"""
@hops.component(
    "/crvTangentAt",
    name="Tangent At",
    nickname="CrvTangentAt",
    description="Curve tangent at parameter",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("Parameter", "T", "Parameter to evaluate")
    ],
    outputs=[hs.HopsVector("Tangent", "T", "Tangent")]
)
def crv_tangent_at(curve: rhino3dm.Curve, parameter):
    return curve.TangentAt(parameter)

"""
CurvatureAt(t)
Evaluate the curvature vector at a curve parameter.

Parameters:	t (float) – Evaluation parameter.
Returns:	Curvature vector of the curve at the parameter t.
Return type:	rhino3dm.Vector3d
"""
@hops.component(
    "/crvCurvatureAt",
    name="Curvature At",
    nickname="CrvCurvatureAt",
    description="Curve curvature at parameter",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("Parameter", "T", "Parameter to evaluate")
    ],
    outputs=[hs.HopsVector("Curvature", "C", "Curvature")]
)
def crv_curvature_at(curve: rhino3dm.Curve, parameter):
    return curve.CurvatureAt(parameter)

"""
curve frame at parameter
FrameAt(t)
Returns a 3d frame at a parameter.

Parameters:	t (float) – Evaluation parameter.
Returns:	tuple (bool, rhino3dm.Plane)
True on success, False on failure.
The frame is returned here.
Return type:	(bool, rhino3dm.Plane)
"""
@hops.component(
    "/crvFrameAt",
    name="Frame At",
    nickname="CrvFrameAt",
    description="Curve frame at parameter",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("Parameter", "T", "Parameter to evaluate")
    ],
    # need to output an origin point and vectors for creating a plane in the UI
    outputs=[
        hs.HopsBoolean("Success", "Success", "Success"), 
        hs.HopsPoint("Origin", "O", "Origin"),
        hs.HopsVector("X", "X", "X"),
        hs.HopsVector("Y", "Y", "Y"),
        hs.HopsVector("Z", "Z", "Z")
    ]
)
def crv_frame_at(curve: rhino3dm.Curve, parameter):
    success, frame = curve.FrameAt(parameter)
    return success, frame.Origin, frame.XAxis, frame.YAxis, frame.ZAxis

"""
curve get curve parameter form nurbs from parameter
GetCurveParameterFromNurbsFormParameter(nurbsParameter)
Convert a NURBS curve parameter to a curve parameter.

Parameters:	nurbsParameter (float) – NURBS form parameter.
Returns:	tuple (bool, float)
True on success, False on failure.
Curve parameter.
Return type:	(bool, float)
"""
@hops.component(
    "/crvGetCurveParameterFromNurbsFormParameter",
    name="Get Curve Parameter From Nurbs Form Parameter",
    nickname="CrvGetCurveParameterFromNurbsFormParameter",
    description="Curve get curve parameter from nurbs form parameter",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("NurbsFormParameter", "N", "Nurbs form parameter to evaluate")
    ],
    outputs=[
            hs.HopsBoolean("Success", "Success", "Success"), 
            hs.HopsNumber("CurveParameter", "P", "Curve parameter")]
)
def crv_get_curve_parameter_from_nurbs_form_parameter(curve: rhino3dm.Curve, nurbs_form_parameter):
    success, curve_parameter = curve.GetCurveParameterFromNurbsFormParameter(nurbs_form_parameter)
    return success, curve_parameter

"""
curve get nurbs form parameter from curve parameter
GetNurbsFormParameterFromCurveParameter(curveParameter)
Convert a curve parameter to a NURBS curve parameter.

Parameters:	curveParameter (float) – Curve parameter.
Returns:	tuple (bool, float)
True on success, False on failure.
NURBS form parameter.
Return type:	(bool, float)
"""
@hops.component(
    "/crvGetNurbsFormParameterFromCurveParameter",
    name="Get Nurbs Form Parameter From Curve Parameter",
    nickname="CrvGetNurbsFormParameterFromCurveParameter",
    description="Curve get nurbs form parameter from curve parameter",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("CurveParameter", "P", "Curve parameter to evaluate")
    ],
    outputs=[
            hs.HopsBoolean("Success", "Success", "Success"), 
            hs.HopsNumber("NurbsFormParameter", "N", "Nurbs form parameter")]
)
def crv_get_nurbs_form_parameter_from_curve_parameter(curve: rhino3dm.Curve, curve_parameter):
    success, nurbs_form_parameter = curve.GetNurbsFormParameterFromCurveParameter(curve_parameter)
    return success, nurbs_form_parameter

"""
curve trim(t0, t1)
Trim(t0, t1)
Removes portions of the curve outside the specified interval.

Parameters:	
t0 (float) – Start of the trimming interval. Portions of the curve before curve(t0) are removed.
t1 (float) – End of the trimming interval. Portions of the curve after curve(t1) are removed.
Returns:	
Trimmed portion of this curve is successful, None on failure.

Return type:	
rhino3dm.Curve
"""
@hops.component(
    "/crvTrim",
    name="Trim",
    nickname="CrvTrim",
    description="Curve trim",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("Start", "S", "Start of the trimming interval"),
        hs.HopsNumber("End", "E", "End of the trimming interval")
    ],
    outputs=[hs.HopsCurve("Trimmed", "T", "Trimmed curve")]
)
def crv_trim(curve: rhino3dm.Curve, start, end):
    return curve.Trim(start, end)

"""
curve split(t)
Split(t)
Splits (divides) the curve at the specified parameter. 
The parameter must be in the interior of the curve’s domain.

Parameters:	t (float) – Parameter to split 
the curve at in the interval returned by Domain().
Returns:	Two curves on success, None on failure.
Return type:	rhino3dm.Curve[]
"""
@hops.component(
    "/crvSplit",
    name="Split",
    nickname="CrvSplit",
    description="Curve split",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("Parameter", "T", "Parameter to split the curve at in the interval returned by Domain()")
    ],
    outputs=[hs.HopsCurve("First", "F", "First curve"), hs.HopsCurve("Second", "S", "Second curve")]
)
def crv_split(curve: rhino3dm.Curve, parameter):
    return curve.Split(parameter)

"""
curve to nurbs curve
ToNurbsCurve()
Constructs a NURBS curve representation of this curve.

Returns:	NURBS representation of the curve on success, None on failure.
Return type:	rhino3dm.NurbsCurve
"""
@hops.component(
    "/crvToNurbsCurve",
    name="To Nurbs Curve",
    nickname="CrvToNurbsCurve",
    description="Curve to nurbs curve",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate")
    ],
    outputs=[hs.HopsCurve("Nurbs", "N", "Nurbs curve")]
)
def crv_to_nurbs_curve(curve: rhino3dm.Curve):
    return curve.ToNurbsCurve()

"""
███████╗██╗   ██╗██████╗ ███████╗ █████╗  ██████╗███████╗███████╗
██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝
███████╗██║   ██║██████╔╝█████╗  ███████║██║     █████╗  ███████╗
╚════██║██║   ██║██╔══██╗██╔══╝  ██╔══██║██║     ██╔══╝  ╚════██║
███████║╚██████╔╝██║  ██║██║     ██║  ██║╚██████╗███████╗███████║
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝╚══════╝                                                                                                               
"""

"""
surface is solid
IsSolid
bool: Gets a values indicating whether a surface is solid.
"""
@hops.component(
    "/srfIsSolid",
    name="Is Solid",
    nickname="SrfIsSolid",
    description="Surface is solid",
    inputs=[
        hs.HopsSurface("Surface", "S", "Surface to evaluate")
    ],
    outputs=[hs.HopsBoolean("IsSolid", "S", "Is solid")]
)
def srf_is_solid(surface: rhino3dm.Surface):
    return surface.IsSolid

"""
surface set domain
SetDomain(direction, domain)
Sets the domain in a direction.

Parameters:	
direction (int) – 0 sets first parameter’s domain, 1 sets second parameter’s domain.
domain (rhino3dm.Interval) – A new domain to be assigned.
Returns:	
True if setting succeeded, otherwise false.

Return type:	
bool
"""

"""
@hops.component(
    "/srfSetDomain",
    name="Set Domain",
    nickname="SrfSetDomain",
    description="Surface set domain",
    inputs=[
        hs.HopsSurface("Surface", "S", "Surface to evaluate"),
        hs.HopsNumber("Direction", "D", "Direction"),
        # this is going to need an interval and no hs.HopsInterval exists currently
        # need to create and interval component for this to work
        # put on hold until I can figure out how to do this
        hs.HopsInterval("Domain", "D", "Domain")
    ],
    outputs=[hs.HopsBoolean("Success", "S", "Success")]
)
def srf_set_domain(surface: rhino3dm.Surface, direction, domain):
    return surface.SetDomain(direction, domain)
"""

"""
surface degree(direction)
Degree(direction)
Returns the maximum algebraic degree of any span 
(or a good estimate if curve spans are not algebraic).

Parameters:	direction (int) – 
0 gets first parameter’s domain, 
1 gets second parameter’s domain.
Returns:	The maximum degree.
Return type:	int
"""
@hops.component(
    "/srfDeg",
    name="Degree",
    nickname="SrfDegree",
    description="Surface degree",
    inputs=[
        hs.HopsSurface("Surface", "S", "Surface to evaluate"),
        hs.HopsInteger("Direction", "D", "Direction")
    ],
    outputs=[hs.HopsNumber("Degree", "D", "Degree")]
)
def srf_deg(surface: rhino3dm.Surface, direction):
    return surface.Degree(direction)

"""
surface span count (direction)
SpanCount(direction)
Gets number of smooth nonempty spans in the parameter direction.

Parameters:	direction (int) – 
0 gets first parameter’s domain, 
1 gets second parameter’s domain.
Returns:	The span count.
Return type:	int
"""
@hops.component(
    "/srfSpanCount",
    name="Span Count",
    nickname="SrfSpanCount",
    description="Surface span count",
    inputs=[
        hs.HopsSurface("Surface", "S", "Surface to evaluate"),
        hs.HopsInteger("Direction", "D", "Direction")
    ],
    outputs=[hs.HopsNumber("SpanCount", "S", "Span count")]
)
def srf_span_count(surface: rhino3dm.Surface, direction):
    return surface.SpanCount(direction)

"""
surface pointAt(u, v)
PointAt(u, v)
Evaluates a point at a given parameter.

Parameters:	
u (float) – evaluation parameters.
v (float) – evaluation parameters.
Returns:	
Point3d.Unset on failure.

Return type:	
rhino3dm.Point3d
"""
@hops.component(
    "/srfPointAt",
    name="Point At",
    nickname="SrfPointAt",
    description="Surface point at",
    inputs=[
        hs.HopsSurface("Surface", "S", "Surface to evaluate"),
        hs.HopsNumber("U", "U", "U"),
        hs.HopsNumber("V", "V", "V")
    ],
    outputs=[hs.HopsPoint("Point", "P", "Point")]
)
def srf_point_at(surface: rhino3dm.Surface, u, v):
    return surface.PointAt(u, v)

"""
surface frame(u, v)
FrameAt(u, v)
Computes the orient plane on a surface given a U and V parameter. 
This is the simple evaluation call with no error handling.

Parameters:	
u (float) – A first parameter.
v (float) – A second parameter.
Returns:	
tuple (bool, rhino3dm.Plane) 
BUT WE MUST RETURN AN ORIGIN AND THREE VECTORS INSTEAD FOR NOW

True if this operation succeeded; otherwise false.
A frame plane that will be computed during this call.
Return type:	
(bool, rhino3dm.Plane)
"""


@hops.component(
    "/srfFrame11",
    name="Frame",
    nickname="SrfFrame",
    description="Surface frame",
    inputs=[
        hs.HopsSurface("Surface", "S", "Surface to evaluate"),
        hs.HopsNumber("U", "U", "U"),
        hs.HopsNumber("V", "V", "V"),
    ],
    outputs=[
        hs.HopsBoolean("Success", "S", "Success"), 
        hs.HopsPoint("Origin", "O", "Origin"),
        hs.HopsVector("X", "X", "X"),
        hs.HopsVector("Y", "Y", "Y"),
        hs.HopsVector("Z", "Z", "Z")
    ]
)
def srf_frame11(surface: rhino3dm.Surface, u, v):
    success, frame = surface.FrameAt(u, v)
    # origin and vectors are not returned by the frameAt function
    # we need to manually compute them
    origin = surface.PointAt(u, v)
    x = frame.XAxis
    y = frame.YAxis
    z = frame.ZAxis
    return success, origin, x, y, z

"""
surface domain(direction)
Domain(direction)
Gets the domain in a direction.

Parameters:	direction (int) – 0 gets first parameter, 1 gets second parameter.
Returns:	An interval value.
Return type:	rhino3dm.Interval
"""

"""
██╗███╗   ██╗████████╗███████╗██████╗ ██╗   ██╗ █████╗ ██╗     
██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗██║   ██║██╔══██╗██║     
██║██╔██╗ ██║   ██║   █████╗  ██████╔╝██║   ██║███████║██║     
██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══██║██║     
██║██║ ╚████║   ██║   ███████╗██║  ██║ ╚████╔╝ ██║  ██║███████╗
╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝
"""
"""
create interval(t0, t1)
Interval(t0, t1)
Initializes a new instance of the Rhino.Geometry.Interval class.

Parameters:	
t0 (float) – The first value.
t1 (float) – The second value.
T0
float: Gets or sets the lower bound of the Interval.

T1
float: Gets or sets the upper bound of the Interval.
"""
@hops.component(
    "/intervalConcat",
    name="Interval",
    nickname="Intv",
    description="Interval",
    inputs=[
        hs.HopsNumber("T0", "T0", "T0"),
        hs.HopsNumber("T1", "T1", "T1")
    ],
    # output t0 (float) – The first value.
    # output t1 (float) – The second value.
    outputs=[
        hs.HopsNumber("T0", "T0", "T0"), 
        hs.HopsNumber("T1", "T1", "T1"),
        hs.HopsString("concatenated", "C", "Concatenated")
        ]
)
def intervalConcat(t0, t1):
    num_t0 = float(t0)
    num_t1 = float(t1)
    concatenated = str(num_t0) + " to " + str(num_t1)
    return num_t0, num_t1, concatenated

"""
surface domain(direction)
Domain(direction)
Gets the domain in a direction.

Parameters:	direction (int) – 
0 gets first parameter, 
1 gets second parameter.
Returns:	An interval value.
Return type:	rhino3dm.Interval
"""

"""
@hops.component(
    "/srfDomain2",
    name="Domain",
    nickname="SrfDomain",
    description="Surface domain",
    inputs=[
        hs.HopsSurface("Surface", "S", "Surface to evaluate"),
        hs.HopsNumber("Umin", "Umin", "Umin"),
        hs.HopsNumber("Umax", "Umax", "Umax"),
        hs.HopsNumber("Vmin", "Vmin", "Vmin"),
        hs.HopsNumber("Vmax", "Vmax", "Vmax")
    ],
    outputs=[
        hs.HopsBoolean("Success", "S", "Success"), 
        hs.HopsPoint("Start", "S", "Start"),
        ]
)
"""

"""
NormalAt(u, v)
Computes the surface normal at a point. This is the simple evaluation call - it does not support error handling.

Parameters:	
u (float) – A U parameter.
v (float) – A V parameter.
Returns:	
The normal.

Return type:	
rhino3dm.Vector3d
"""
@hops.component(
    "/srfNorAt",
    name="NormalAt",
    nickname="SrfNorAt",
    description="Surface normal at",
    inputs=[
        hs.HopsSurface("Surface", "S", "Surface to evaluate"),
        hs.HopsNumber("U", "U", "U"),
        hs.HopsNumber("V", "V", "V"),
    ],
    outputs=[
        hs.HopsBoolean("Success", "S", "Success"), 
        hs.HopsVector("Normal", "N", "Normal"),
        ]
)
def srf_nor_at(surface: rhino3dm.Surface, u, v):
    success, normal = surface.NormalAt(u, v)
    return success, normal

"""
██████╗ ██╗      █████╗ ███╗   ██╗███████╗███████╗
██╔══██╗██║     ██╔══██╗████╗  ██║██╔════╝██╔════╝
██████╔╝██║     ███████║██╔██╗ ██║█████╗  ███████╗
██╔═══╝ ██║     ██╔══██║██║╚██╗██║██╔══╝  ╚════██║
██║     ███████╗██║  ██║██║ ╚████║███████╗███████║
╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝
"""

"""
Plane()
Plane constructor

Plane(origin, normal)
Constructs a plane from a point and a normal vector.

Parameters:	
origin (rhino3dm.Point3d) – Origin point of the plane.
normal (rhino3dm.Vector3d) – Non-zero normal to the plane.
"""
@hops.component(
    "/plane4",
    name="Plane",
    nickname="Plane",
    description="Plane",
    inputs=[
        hs.HopsPoint("Origin", "O", "Origin"),
        hs.HopsVector("Normal", "N", "Normal"),
    ],
    outputs=[
        hs.HopsBoolean("Success", "S", "Success"),
        hs.HopsPoint("Origin", "O", "Origin"),
        hs.HopsVector("Normal", "N", "Normal"),
        ]
)
def plane4(origin, normal):
    return True, origin, normal

"""
plane from equation Ax+By+Cz+D=0
Plane()
Constructs a plane from an equation Ax+By+Cz+D=0.
"""


@hops.component(
    "/planeFromEquation2",
    name="Plane",
    nickname="Plane",
    description="Plane",
    inputs=[    
        hs.HopsNumber("A", "A", "A"),
        hs.HopsNumber("x", "x", "x"),
        hs.HopsNumber("B", "B", "B"),
        hs.HopsNumber("y", "y", "y"),
        hs.HopsNumber("C", "C", "C"),
        hs.HopsNumber("z", "z", "z"),
        hs.HopsNumber("D", "D", "D"),
    ],
    outputs=[
        hs.HopsBoolean("Success", "S", "Success"),
        # Constructs a plane from an equation Ax+By+Cz+D=0
        hs.HopsNumber("slope", "S", "Slope"),
        hs.HopsPoint("origin", "O", "Origin"),
        hs.HopsVector("normal", "N", "Normal"),

        ]
)
def planeFromEquation2(a, x, b, y, c, z, d):
    success = True
    slope = float(a) / float(d)
    origin = rhino3dm.Point3d(float(x), float(y), float(z))
    normal = rhino3dm.Vector3d(float(b), float(c), float(d))
    return success, slope, origin, normal

    
#plane from origin and 2 vectors
"""
Plane()
Constructs a plane from an origin point and two vectors.
"""

"""
@hops.component(
    "/planeFromOriginAnd2Vectors",
    name="Plane",
    nickname="Plane",
    description="Plane",
    inputs=[
        hs.HopsPoint("Origin", "O", "Origin"),
        hs.HopsVector("X", "X", "X"),
        hs.HopsVector("Y", "Y", "Y"),
    ],
    outputs=[
        hs.HopsBoolean("Success", "S", "Success"),
        hs.HopsPoint("Origin", "O", "Origin"),
        hs.HopsVector("Normal", "N", "Normal"),
        ]
)
"""

"""
create plane surface
PlaneSurface()
PlaneSurface constructor

PlaneSurface()
PlaneSurface constructor
"""

# create plane surface
@hops.component(
    "/planeSurface17",
    name="PlaneSurface",
    nickname="PlaneSurface",
    description="PlaneSurface",
    inputs=[
        hs.HopsSurface("Surface", "S", "Surface"),
        hs.HopsPoint("Origin", "O", "Origin"),
        hs.HopsVector("Normal", "N", "Normal"),
        hs.HopsNumber("uMin", "uMin", "uMin"),
        hs.HopsNumber("uMax", "uMax", "uMax"),
        hs.HopsNumber("vMin", "vMin", "vMin"),
        hs.HopsNumber("vMax", "vMax", "vMax"),
    ],
    outputs=[
        hs.HopsBoolean("Success", "S", "Success"),
        hs.HopsSurface("Surface", "S", "Surface"),
        ]
)
def planeSurface17(surface, origin, normal, uMin, uMax, vMin, vMax):
    success = True
    plane = rhino3dm.Plane(origin, normal)
    planeSurface = rhino3dm.PlaneSurface(plane, uMin, uMax, vMin, vMax)
    return success, planeSurface






"""
██████╗  ██████╗ ██╗███╗   ██╗████████╗     ██████╗ ██████╗ ██╗██████╗ 
██╔══██╗██╔═══██╗██║████╗  ██║╚══██╔══╝    ██╔════╝ ██╔══██╗██║██╔══██╗
██████╔╝██║   ██║██║██╔██╗ ██║   ██║       ██║  ███╗██████╔╝██║██║  ██║
██╔═══╝ ██║   ██║██║██║╚██╗██║   ██║       ██║   ██║██╔══██╗██║██║  ██║
██║     ╚██████╔╝██║██║ ╚████║   ██║       ╚██████╔╝██║  ██║██║██████╔╝
╚═╝      ╚═════╝ ╚═╝╚═╝  ╚═══╝   ╚═╝        ╚═════╝ ╚═╝  ╚═╝╚═╝╚═════╝ 
"""

"""
PointGrid
classrhino3dm.PointGrid
PointGrid()
PointGrid constructor
"""

"""
# create a point grid
@hops.component(
    "/pointGrid8",
    name="PointGrid",
    nickname="PointGrid",
    description="PointGrid",
    inputs=[
        hs.HopsPoint("Origin", "O", "Origin"),
        hs.HopsVector("X", "X", "X"),
        hs.HopsVector("Y", "Y", "Y"),
        hs.HopsInteger("Ucount", "Ucount", "Ucount"),
        hs.HopsInteger("Vcount", "Vcount", "Vcount"),
    ],
    outputs=[
        hs.HopsBoolean("Success", "S", "Success"),
        hs.HopsPoint("Point", "P", "Point", access=hs.HopsParamAccess.LIST),
        ]
)
def pointGrid8(origin, x, y, ucount, vcount):
    success = True
    point = rhino3dm.PointGrid(origin, x, y, ucount, vcount)
    print(type(point))
    print("Hello Wickerson")
    return success, point
"""
"""
██╗   ██╗███████╗ ██████╗████████╗ ██████╗ ██████╗ ███████╗
██║   ██║██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝
██║   ██║█████╗  ██║        ██║   ██║   ██║██████╔╝███████╗
╚██╗ ██╔╝██╔══╝  ██║        ██║   ██║   ██║██╔══██╗╚════██║
 ╚████╔╝ ███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║███████║
  ╚═══╝  ╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
"""
"""
classrhino3dm.Vector2d
Vector2d(x, y)
Initializes a new instance of the vector based on two, X and Y, components.

Parameters:	
x (float) – The X (first) component.
y (float) – The Y (second) component.
X
float: Gets or sets the X (first) component of this vector.

Y
float: Gets or sets the Y (second) component of this vector.
"""
    
# create vector 2d
@hops.component(
    "/vector2dim",
    name="Vector2d",
    nickname="Vector2d",
    description="Vector2d",
    inputs=[
        hs.HopsNumber("X", "X", "X"),
        hs.HopsNumber("Y", "Y", "Y"),
    ],
    outputs=[
        hs.HopsBoolean("Success", "S", "Success"),
        hs.HopsVector("Vector2d", "V", "Vector2d"),
        ]
)
def vector2dim(x: float, y: float):
    success = True
    vector2d = rhino3dm.Vector3d(x, y, 0)
    return success, vector2d

"""
classrhino3dm.Vector3d
Vector3d(x, y, z)
Initializes a new instance of a vector, using its three components.

Parameters:	
x (float) – The X (first) component.
y (float) – The Y (second) component.
z (float) – The Z (third) component.
X
float: Gets or sets the X (first) component of the vector.

Y
float: Gets or sets the Y (second) component of the vector.

Z
float: Gets or sets the Z (third) component of the vector.
"""
# create vector 3d
@hops.component(
    "/vector3dim",
    name="Vector3d",
    nickname="Vector3d",
    description="Vector3d",
    inputs=[
        hs.HopsNumber("X", "X", "X"),
        hs.HopsNumber("Y", "Y", "Y"),
        hs.HopsNumber("Z", "Z", "Z"),
    ],
    outputs=[
        hs.HopsBoolean("Success", "S", "Success"),
        hs.HopsVector("Vector3d", "V", "Vector3d"),
        ]
)
def vector3dim(x: float, y: float, z: float):
    success = True
    vector3d = rhino3dm.Vector3d(x, y, z)
    return success, vector3d

"""
 ██████╗██╗   ██╗██████╗ ██╗   ██╗███████╗███████╗
██╔════╝██║   ██║██╔══██╗██║   ██║██╔════╝██╔════╝
██║     ██║   ██║██████╔╝██║   ██║█████╗  ███████╗
██║     ██║   ██║██╔══██╗╚██╗ ██╔╝██╔══╝  ╚════██║
╚██████╗╚██████╔╝██║  ██║ ╚████╔╝ ███████╗███████║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚══════╝
                                                  
"""

"""
classrhino3dm.Line
Line(from, to)
Constructs a new line segment between two points.

Parameters:	
from (rhino3dm.Point3d) – Start point of line.
to (rhino3dm.Point3d) – End point of line.
From
rhino3dm.Point3d: Start point of line segment.

To
rhino3dm.Point3d: End point of line segment.
"""
# create line
@hops.component(
    "/lineFromAB",
    name="LineFromAB",
    nickname="LineFromAB",
    description="LineFromAtoB",
    inputs=[
        hs.HopsPoint("A", "A", "A"),
        hs.HopsPoint("B", "B", "B"),
    ],
    outputs=[
        hs.HopsBoolean("Success", "S", "Success"),
        hs.HopsCurve("Line", "L", "Line"),
        ]
)
def lineFromAB(a: rhino3dm.Point, b: rhino3dm.Point):
    success = True
    line = rhino3dm.LineCurve(a, b)
    return success, line

"""
 █████╗ ██████╗  ██████╗
██╔══██╗██╔══██╗██╔════╝
███████║██████╔╝██║     
██╔══██║██╔══██╗██║     
██║  ██║██║  ██║╚██████╗
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝                                              
"""
"""
classrhino3dm.Arc
Arc(circle, angleRadians)
Initializes a new instance of an arc from a base circle and an angle.

Parameters:	
circle (Circle) – Circle to base arc upon.
angleRadians (float) – Sweep angle of arc (in radians)
"""
# create and arc from a circle
@hops.component(
    "/arcCircle",
    name="ArcFromCircle",
    nickname="ArcFromCircle",
    description="ArcFromCircle",
    inputs=[
        hs.HopsCurve("Circle", "C", "Circle"),
        hs.HopsNumber("Angle", "A", "Angle"),
    ],
    outputs=[
        hs.HopsBoolean("Success", "S", "Success"),
        hs.HopsCurve("Arc", "A", "Arc"),
        ]
)
def arcCircle(circle: rhino3dm.Curve, angle: float):
    success = True
    arc = rhino3dm.Arc(circle, angle)
    return success, arc

"""
Arc(center, radius, angleRadians)
Initializes a new horizontal arc at the given center point, with a custom radius and angle.

Parameters:	
center (rhino3dm.Point3d) – Center point of arc.
radius (float) – Radius of arc.
angleRadians (float) – Sweep angle of arc (in radians)
"""
# create an arc from a center point
@hops.component(
    "/arcCenter",
    name="ArcFromCenter",
    nickname="ArcFromCenter",
    description="ArcFromCenter",
    inputs=[
        hs.HopsPoint("Center", "C", "Center"),
        hs.HopsNumber("Radius", "R", "Radius"),
        hs.HopsNumber("Angle", "A", "Angle"),
    ],
    outputs=[
        hs.HopsBoolean("Success", "S", "Success"),
        hs.HopsCurve("Arc", "A", "Arc"),
        ]
)
def arcCenter(center: rhino3dm.Point, radius: float, angle: float):
    success = True
    arc = rhino3dm.Arc(center, radius, angle)
    return success, arc 

"""
Arc(startPoint, pointOnInterior, endPoint)
Initializes a new arc through three points. If the points are coincident or co-linear, this will result in an Invalid arc.

Parameters:	
startPoint (rhino3dm.Point3d) – Start point of arc.
pointOnInterior (rhino3dm.Point3d) – Point on arc interior.
endPoint (rhino3dm.Point3d) – End point of arc.
"""
# create an arc from three points
@hops.component(
    "/arcPoints",
    name="ArcFromPoints",
    nickname="ArcFromPoints",
    description="ArcFromPoints",
    inputs=[
        hs.HopsPoint("Start", "S", "Start"),
        hs.HopsPoint("Interior", "I", "Interior"),
        hs.HopsPoint("End", "E", "End"),
    ],
    outputs=[
        hs.HopsBoolean("Success", "S", "Success"),
        hs.HopsCurve("Arc", "A", "Arc"),
        ]
)
def arcPoints(start: rhino3dm.Point, interior: rhino3dm.Point, end: rhino3dm.Point):
    success = True
    arc = rhino3dm.Arc(start, interior, end)
    return success, arc

"""
Arc(pointA, tangentA, pointB)
Initializes a new arc from end points and a tangent vector. If the tangent is parallel with the endpoints this will result in an Invalid arc.

Parameters:	
pointA (rhino3dm.Point3d) – Start point of arc.
tangentA (rhino3dm.Vector3d) – Tangent at start of arc.
pointB (rhino3dm.Point3d) – End point of arc.
"""
# create an arc from two points and a tangent
@hops.component(
    "/arcTangent",
    name="ArcFromTangent",
    nickname="ArcFromTangent",
    description="ArcFromTangent",
    inputs=[
        hs.HopsPoint("Start", "S", "Start"),
        hs.HopsVector("Tangent", "T", "Tangent"),
        hs.HopsPoint("End", "E", "End"),
    ],
    outputs=[
        hs.HopsBoolean("Success", "S", "Success"),
        hs.HopsCurve("Arc", "A", "Arc"),    
        ]
)
def arcTangent(start: rhino3dm.Point, tangent: rhino3dm.Vector, end: rhino3dm.Point):
    success = True
    arc = rhino3dm.Arc(start, tangent, end)
    return success, arc

"""
ClosestPoint(testPoint)
Computes the point on an arc that is closest to a test point.

Parameters:	testPoint (rhino3dm.Point3d) – Point to get close to.
Returns:	The point on the arc that is closest to testPoint. If testPoint is the center of the arc, then the starting point of the arc is returned. UnsetPoint on failure.
Return type:	rhino3dm.Point3d
"""
# get the closest point on an arc
@hops.component(
    "/arcClosestPoint",
    name="ArcClosestPoint",
    nickname="ArcClosestPoint",
    description="ArcClosestPoint",
    inputs=[
        hs.HopsCurve("Arc", "A", "Arc"),
        hs.HopsPoint("Point", "P", "Point"),
    ],
    outputs=[
        hs.HopsBoolean("Success", "S", "Success"),
        hs.HopsPoint("Closest", "C", "Closest"),
        ]
)
def arcClosestPoint(arc: rhino3dm.Curve, point: rhino3dm.Point):
    success = True
    closest = arc.ClosestPoint(point)
    return success, closest

"""
sorting algorithms
"""




if __name__ == "__main__":
    app.run(debug=True)
