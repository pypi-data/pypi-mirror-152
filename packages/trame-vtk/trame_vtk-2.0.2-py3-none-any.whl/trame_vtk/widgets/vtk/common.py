from trame_client.widgets.core import AbstractElement
from trame_vtk.modules import common

MODULE = None


def use_module(m):
    global MODULE
    MODULE = m


def activate_module_for(server, vtk_or_paraview_obj):
    if MODULE is None:
        if vtk_or_paraview_obj.IsA("vtkSMRemoteObject"):
            from trame_vtk.modules import paraview

            use_module(paraview)
            server.enable_module(paraview)
        else:
            from trame_vtk.modules import vtk

            use_module(vtk)
            server.enable_module(vtk)


class HtmlElement(AbstractElement):
    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)
        if self.server:
            self.server.enable_module(common)


class VtkAlgorithm(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtk-algorithm", children, **kwargs)
        self._attr_names += ["port", "vtk_class", "state"]


class VtkCellData(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtk-cell-data", children, **kwargs)


class VtkDataArray(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("vtk-data-array", **kwargs)
        self._attr_names += [
            "name",
            "registration",
            "type",
            "values",
            "number_of_components",
        ]


class VtkFieldData(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtk-field-data", children, **kwargs)


class VtkGeometryRepresentation(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtk-geometry-representation", children, **kwargs)
        self._attr_names += [
            "id",
            "color_map_preset",
            "color_data_range",
            "actor",
            "mapper",
            "property",
        ]


class VtkGlyphRepresentation(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtk-glyph-representation", children, **kwargs)
        self._attr_names += [
            "color_map_preset",
            "color_data_range",
            "actor",
            "mapper",
            "property",
        ]


class VtkMesh(HtmlElement):
    def __init__(
        self,
        name,
        dataset=None,
        field_to_keep=None,
        point_arrays=None,
        cell_arrays=None,
        **kwargs,
    ):
        super().__init__("vtk-mesh", **kwargs)
        self.__name = name
        self.__dataset = dataset
        self.__field_to_keep = field_to_keep
        self.__point_arrays = point_arrays
        self.__cell_arrays = cell_arrays
        self._attr_names += ["port", "state"]
        if dataset:
            activate_module_for(self.server, dataset)
            self._attributes["state"] = f':state="{name}"'
            self.update()

    def set_dataset(self, dataset):
        """
        Change this mesh's internal dataset and update shared state"""
        self.__dataset = dataset
        self.update()

    def update(self, **kwargs):
        """
        Propagate changes in internal data to shared state
        """
        if self.__dataset:
            self.server.state[self.__name] = MODULE.mesh(
                self.__dataset,
                field_to_keep=kwargs.get("field_to_keep", self.__field_to_keep),
                point_arrays=kwargs.get("point_arrays", self.__point_arrays),
                cell_arrays=kwargs.get("cell_arrays", self.__cell_arrays),
            )


class VtkPointData(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtk-point-data", children, **kwargs)


class VtkPolyData(HtmlElement):
    def __init__(self, name, children=None, dataset=None, **kwargs):
        super().__init__("vtk-polydata", children, **kwargs)
        self.__name = name
        self.__dataset = dataset
        self._attr_names += [
            "port",
            "verts",
            "lines",
            "polys",
            "strips",
            "connectivity",
        ]
        if dataset:
            activate_module_for(self.server, dataset)
            self._attributes["bind"] = f'v-bind="{name}.mesh"'
            self.update()

    def set_dataset(self, dataset):
        """
        Change this polydata's internal dataset and update shared state
        """
        self.__dataset = dataset
        self.update()

    def update(self):
        """
        Propagate changes in internal data to shared state
        """
        if self.__dataset:
            self.server.state[self.__name] = MODULE.mesh(self.__dataset)


class VtkReader(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__("vtk-reader", **kwargs)
        self._attr_names += [
            "parse_as_array_buffer",
            "parse_as_text",
            "port",
            "render_on_update",
            "reset_camera_on_update",
            "url",
            "vtk_class",
        ]


class VtkRemoteLocalView(HtmlElement):
    """
    The VtkRemoteLocalView component is a blend of VtkLocalView and VtkRemoteView where the user can choose dynamically which mode they want to be in. When instantiating a VtkRemoteLocalView several variables and triggers will be created for you to more easily control your view.

    >>> rl_view = vtk.VtkRemoteLocalView(
    ...   view=...,                # Instance of the view (required)
    ...                            # - VTK: vtkRenderWindow
    ...                            # - Paraview: viewProxy
    ...   # Just VtkRemoteLocalView params
    ...   namespace=...,           # Prefix for variables and triggers. See below. (required)
    ...   mode="local",            # Decide between local or remote. See below.
    ...
    ...   # VtkRemoteView params
    ...   **remote_view_params,
    ...
    ...   # VtkLocalView params
    ...   **local_view_params,
    ... )
    """

    def __init__(self, view, enable_rendering=True, **kwargs):
        super().__init__("vtk-remote-local-view", **kwargs)

        activate_module_for(self.server, view)

        __ns = kwargs.get("namespace", "view")
        self.__mode_key = f"{__ns}Mode"
        self.__scene_id = f"{__ns}Scene"
        self.__view_key_id = f"{__ns}Id"
        self.__ref = kwargs.get("ref", __ns)
        self.__rendering = enable_rendering
        self.__namespace = __ns

        # !!! HACK !!!
        # Allow user to configure view mode by providing (..., local/remote) and or "local/remote"
        __mode_expression = kwargs.get("mode", self.__mode_key)
        __mode_start = "remote"
        if isinstance(__mode_expression, (tuple, list)):
            if len(__mode_expression) == 2:
                __mode_expression, __mode_start = __mode_expression
            else:
                __mode_expression = __mode_expression[0]
        elif __mode_expression in ["local", "remote"]:
            __mode_start = __mode_expression
            __mode_expression = self.__mode_key

        self._attributes["mode"] = f':mode="{__mode_expression}"'
        # !!! HACK !!!

        self.server.state[self.__view_key_id] = MODULE.id(view)
        self.__view = view
        self.__wrapped_view = MODULE.view(view, name=__ns, mode=__mode_start)

        # Provide mandatory attributes
        self._attributes["ref"] = f'ref="{self.__ref}"'
        self._attributes["view_id"] = f':viewId="{self.__view_key_id}"'
        self._attributes["view_state"] = f':viewState="{self.__scene_id}"'
        self._attributes["namespace"] = f'namespace="{__ns}"'

        self._attr_names += [
            # "mode", # <--- Managed by hand above
            "context_name",
            "interactive_quality",
            "interactive_ratio",
            ("interactor_events", "interactorEvents"),
            "interactor_settings",
            ("box_selection", "boxSelection"),
        ]
        self._event_names += [
            ("box_selection_change", "BoxSelection"),
            "StartAnimation",
            "Animation",
            "EndAnimation",
            "MouseEnter",
            "MouseLeave",
            "StartMouseMove",
            "MouseMove",
            "EndMouseMove",
            "LeftButtonPress",
            "LeftButtonRelease",
            "MiddleButtonPress",
            "MiddleButtonRelease",
            "RightButtonPress",
            "RightButtonRelease",
            "KeyPress",
            "KeyDown",
            "KeyUp",
            "StartMouseWheel",
            "MouseWheel",
            "EndMouseWheel",
            "StartPinch",
            "Pinch",
            "EndPinch",
            "StartPan",
            "Pan",
            "EndPan",
            "StartRotate",
            "Rotate",
            "EndRotate",
            "Button3D",
            "Move3D",
            "StartPointerLock",
            "EndPointerLock",
            "StartInteraction",
            "Interaction",
            "EndInteraction",
        ]

    def update_geometry(self, reset_camera=False):
        """
        Force update to geometry
        """
        self.server.state[self.__scene_id] = MODULE.scene(self.__view, reset_camera)

    def update_image(self, reset_camera=False):
        """
        Force update to image
        """
        MODULE.push_image(self.__view, reset_camera)

    def set_local_rendering(self, local=True, **kwargs):
        self.server.state[self.__mode_key] = "local" if local else "remote"

    def set_remote_rendering(self, remote=True, **kwargs):
        self.server.state[self.__mode_key] = "remote" if remote else "local"

    def update(self, reset_camera=False, **kwargs):
        # need to do both to keep things in sync
        if self.__rendering:
            self.update_image(reset_camera)
        self.update_geometry(reset_camera)

    def replace_view(self, new_view, **kwargs):
        self.server.state[self.__view_key_id] = MODULE.id(new_view)
        _mode = self.server.state[self.__mode_key]
        self.__view = new_view
        self.__wrapped_view = MODULE.view(
            new_view, name=self.__namespace, mode=_mode, force_replace=True
        )
        self.update()
        self.resize()

    def reset_camera(self, **kwargs):
        self.server.js_call(ref=self.__ref, method="resetCamera")

    def resize(self, **kwargs):
        self.server.js_call(ref=self.__ref, method="resize")

    @property
    def view(self):
        """
        Get linked vtkRenderWindow instance
        """
        return self.__wrapped_view


class VtkRemoteView(HtmlElement):
    """
    The VtkRemoteView component relies on the server for rendering by sending images to the client by binding your vtkRenderWindow to it. This component gives you control over the image size and quality to reduce latency while interacting.

    >>> remote_view = vtk.vtkRemoteView(
    ...   view=...,               # Instance of the view (required)
    ...                           # - VTK: vtkRenderWindow
    ...                           # - Paraview: viewProxy
    ...   ref=...,                # Identifier for this component
    ...   interactive_quality=60, # [0, 100] 0 for fastest render, 100 for best quality
    ...   interactive_ratio=...,  # [0.1, 1] Image size scale factor while interacting
    ...   interactor_events=(     # Enable vtk.js interactor events for method binding
    ...     "events",
    ...     ['EndAnimation'],
    ...   ),
    ...   EndAnimation=end,       # Bind method to the enabled event
    ...
    ...   box_selection=True,     # toggle selection box rendering
    ...   box_selection_change=fn # Bind method to get rect selection
    ... )
    """

    @staticmethod
    def push_image(view):
        """
        Force image `view` to be pushed to the client
        """
        if MODULE:
            MODULE.push_image(view)

    def __init__(self, view, ref="view", **kwargs):
        super().__init__("vtk-remote-view", **kwargs)

        activate_module_for(self.server, view)

        self.__view = view
        self.__ref = ref
        self.__view_key_id = f"{ref}Id"
        self.server.state[self.__view_key_id] = MODULE.id(view)
        self._attributes["ref"] = f'ref="{ref}"'
        self._attributes["view_id"] = f':viewId="{self.__view_key_id}"'
        self._attr_names += [
            "enable_picking",
            "interactive_quality",
            "interactive_ratio",
            ("interactor_events", "interactorEvents"),
            ("box_selection", "boxSelection"),
        ]
        self._event_names += [
            ("box_selection_change", "BoxSelection"),
            "StartAnimation",
            "Animation",
            "EndAnimation",
            "MouseEnter",
            "MouseLeave",
            "StartMouseMove",
            "MouseMove",
            "EndMouseMove",
            "LeftButtonPress",
            "LeftButtonRelease",
            "MiddleButtonPress",
            "MiddleButtonRelease",
            "RightButtonPress",
            "RightButtonRelease",
            "KeyPress",
            "KeyDown",
            "KeyUp",
            "StartMouseWheel",
            "MouseWheel",
            "EndMouseWheel",
            "StartPinch",
            "Pinch",
            "EndPinch",
            "StartPan",
            "Pan",
            "EndPan",
            "StartRotate",
            "Rotate",
            "EndRotate",
            "Button3D",
            "Move3D",
            "StartPointerLock",
            "EndPointerLock",
            "StartInteraction",
            "Interaction",
            "EndInteraction",
        ]

    def update(self, **kwargs):
        """
        Force image to be pushed to client
        """
        MODULE.push_image(self.__view)

    def reset_camera(self, **kwargs):
        self.server.js_call(ref=self.__ref, method="resetCamera")

    def replace_view(self, new_view, **kwargs):
        self.__view = new_view
        self.server.state[self.__view_key_id] = MODULE.id(new_view)
        self.update()
        self.resize()

    def resize(self, **kwargs):
        self.server.js_call(ref=self.__ref, method="resize")


class VtkShareDataset(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtk-share-dataset", children, **kwargs)
        self._attr_names += ["port", "name"]


class VtkLocalView(HtmlElement):
    """
        The VtkLocalView component relies on the server for defining the vtkRenderWindow but then only the geometry is exchanged with the client. The server does not need a GPU as no rendering is happening on the server. The vtkRenderWindow is only used to retrieve the scene data and parameters (coloring by, representations, ...). By relying on the same vtkRenderWindow, you can easily switch from a ``VtkRemoteView`` to a ``VtkLocalView`` or vice-versa. This component gives you controls on how you want to map mouse interaction with the camera. The default setting mimic default VTK interactor style so you will rarely have to override to the ``interactor_settings``.

    >>> local_view = vtk.VtkLocalView(
    ...   view=...,                # Instance of the view (required)
    ...                            # - VTK: vtkRenderWindow
    ...                            # - Paraview: viewProxy
    ...   ref=...,                 # Identifier for this component
    ...   context_name=...,        # Namespace for geometry cache
    ...   interactor_settings=..., # Options for camera controls. See below.
    ...   interactor_events=(      # Enable vtk.js interactor events for method binding
    ...     "events",
    ...     ['EndAnimation'],
    ...    ),
    ...   EndAnimation=end,       # Bind method to the enabled event
    ...
    ...   box_selection=True,     # toggle selection box rendering
    ...   box_selection_change=fn # Bind method to get rect selection
    ... )
    """

    def __init__(self, view, ref="view", **kwargs):
        super().__init__("vtk-local-view", **kwargs)

        activate_module_for(self.server, view)

        self.__scene_id = f"scene_{ref}"
        self.__view = view
        self.__ref = ref
        self._attributes["ref"] = f'ref="{ref}"'
        self._attributes["view_state"] = f':viewState="{self.__scene_id}"'
        self._attr_names += [
            ("interactor_events", "interactorEvents"),
            "interactor_settings",
            "context_name",
            ("box_selection", "boxSelection"),
        ]
        self._event_names += [
            ("box_selection_change", "BoxSelection"),
            "StartAnimation",
            "Animation",
            "EndAnimation",
            "MouseEnter",
            "MouseLeave",
            "StartMouseMove",
            "MouseMove",
            "EndMouseMove",
            "LeftButtonPress",
            "LeftButtonRelease",
            "MiddleButtonPress",
            "MiddleButtonRelease",
            "RightButtonPress",
            "RightButtonRelease",
            "KeyPress",
            "KeyDown",
            "KeyUp",
            "StartMouseWheel",
            "MouseWheel",
            "EndMouseWheel",
            "StartPinch",
            "Pinch",
            "EndPinch",
            "StartPan",
            "Pan",
            "EndPan",
            "StartRotate",
            "Rotate",
            "EndRotate",
            "Button3D",
            "Move3D",
            "StartPointerLock",
            "EndPointerLock",
            "StartInteraction",
            "Interaction",
            "EndInteraction",
        ]
        self.update()

    def update(self, **kwargs):
        """
        Force geometry to be pushed
        """
        self.server.state[self.__scene_id] = MODULE.scene(self.__view)

    def reset_camera(self, **kwargs):
        """
        Move camera to center actors within the frame
        """
        self.server.js_call(ref=self.__ref, method="resetCamera")

    def replace_view(self, new_view, **kwargs):
        self.__view = new_view
        self.server.js_call(self.__ref, "setSynchronizedViewId", MODULE.id(new_view))
        self.update()

    def resize(self, **kwargs):
        self.server.js_call(ref=self.__ref, method="resize")


class VtkView(HtmlElement):
    def __init__(self, children=None, ref="view", **kwargs):
        super().__init__("vtk-view", children, **kwargs)
        self._ref = ref
        self._attributes["ref"] = f'ref="{ref}"'
        self._attr_names += [
            "background",
            "cube_axes_style",
            ("interactor_events", "interactorEvents"),
            "interactor_settings",
            "picking_modes",
            "show_cube_axes",
        ]
        self._event_names += [
            "hover",
            "click",
            "select",
            "resize",
            "StartAnimation",
            "Animation",
            "EndAnimation",
            "MouseEnter",
            "MouseLeave",
            "StartMouseMove",
            "MouseMove",
            "EndMouseMove",
            "LeftButtonPress",
            "LeftButtonRelease",
            "MiddleButtonPress",
            "MiddleButtonRelease",
            "RightButtonPress",
            "RightButtonRelease",
            "KeyPress",
            "KeyDown",
            "KeyUp",
            "StartMouseWheel",
            "MouseWheel",
            "EndMouseWheel",
            "StartPinch",
            "Pinch",
            "EndPinch",
            "StartPan",
            "Pan",
            "EndPan",
            "StartRotate",
            "Rotate",
            "EndRotate",
            "Button3D",
            "Move3D",
            "StartPointerLock",
            "EndPointerLock",
            "StartInteraction",
            "Interaction",
            "EndInteraction",
        ]

    def reset_camera(self, **kwargs):
        """
        Move camera to center actors within the frame
        """
        self.server.js_call(ref=self._ref, method="resetCamera")
