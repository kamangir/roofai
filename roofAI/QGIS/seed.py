# meant to be run inside Python Console in QGIS.
# run `QGIS seed 🌱` to start.

import time
import random
import os
from tqdm import tqdm
import glob

NAME = "roofAI.QGIS"

VERSION = "4.59.1"


HOME = os.getenv("HOME", "")
abcli_object_root = os.path.join(HOME, "storage/abcli")
abcli_QGIS_path_cache = os.path.join(HOME, "git/vancouver-watching/QGIS")
abcli_QGIS_path_shared = os.path.join(HOME, "Downloads/QGIS")
abcli_QGIS_path_server = os.path.join(abcli_QGIS_path_shared, "server")

os.makedirs(abcli_QGIS_path_server, exist_ok=True)


class ABCLI_QGIS_Layer(object):
    def help(self):
        QGIS.log("Q.layer.open()", "open layer.")

    @property
    def filename(self):
        try:
            return iface.activeLayer().dataProvider().dataSourceUri()
        except:
            QGIS.log_error("unknown layer.filename.")
            return ""

    @property
    def name(self):
        filename = self.filename
        return filename.split(os.sep)[-1].split(".")[0] if filename else ""

    @property
    def object_name(self):
        filename = self.filename
        return filename.split(os.sep)[-2] if filename else ""

    def open(self):
        QGIS.open_folder(self.path)

    @property
    def path(self):
        return os.path.dirname(self.filename)


class ABCLI_QGIS_Project(object):
    def help(self):
        QGIS.log("Q.project.open()", "open project.")

    @property
    def name(self):
        return QgsProject.instance().homePath().split(os.sep)[-1]

    def open(self):
        QGIS.open_folder(self.path)

    @property
    def path(self):
        return QgsProject.instance().homePath()


class ABCLI_QGIS_APPLICATION(object):
    def __init__(self, name, icon):
        self.name = name
        self.icon = icon
        QGIS.log(self.name, "", icon=self.icon)

    def log(self, message, note=""):
        QGIS.log(message, note, icon=self.icon)


class ABCLI_QGIS_APPLICATION_VANWATCH(ABCLI_QGIS_APPLICATION):
    def __init__(self):
        super().__init__("vanwatch", "🌈")

    def help(self):
        self.log("vanwatch.ingest()", "ingest a layer now.")
        self.log("vanwatch.list()", "list vanwatch layers.")
        self.log("vanwatch.load(prefix, count)", "load prefix*.")
        self.log("vanwatch.unload(prefix)", "unload prefix*.")
        self.log("vanwatch.update[_cache](push=True)", "update cache.")

    def ingest(self):
        QGIS.seed("abcli_aws_batch source - vanwatch/ingest - count=-1,publish")

    def list(self):
        QGIS.log('to update the cache run "vanwatch update_cache".', icon="🌱")
        return sorted(
            [
                os.path.splitext(os.path.basename(filename))[0]
                for filename in glob.glob(
                    os.path.join(
                        abcli_QGIS_path_cache,
                        "*.geojson",
                    )
                )
            ]
        )

    def load(
        self,
        prefix="",
        count=-1,
        refresh=True,
    ):
        counter = 0
        for layer_name in self.list():
            if not layer_name.startswith(prefix):
                continue

            filename = os.path.join(abcli_QGIS_path_cache, f"{layer_name}.geojson")

            QGIS.load(filename, layer_name, "template-heatmap", refresh=False)
            QGIS.load(filename, layer_name, "template-pin", refresh=False)

            counter += 1
            if counter > count and count != -1:
                break

        if refresh:
            QGIS.refresh()

    def unload(self, prefix="", refresh=True):
        QGIS.log(prefix, icon="🗑️")

        for layer_name in [
            layer_name
            for layer_name in QGIS.list_of_layers()
            if layer_name.startswith(prefix)
        ]:
            QGIS.unload(layer_name, refresh=False)

        if refresh:
            QGIS.refresh()

    def update(self, push=False):
        self.update_cache(push)

    def update_cache(self, push=False):
        QGIS.seed("vanwatch update_cache{}".format(" push" if push else ""))


class ABCLI_QGIS(object):
    def __init__(self):
        self.layer = ABCLI_QGIS_Layer()
        self.project = ABCLI_QGIS_Project()
        self.app_list = []
        self.verbose = False

    def add_application(self, app):
        self.app_list += [app]

    def intro(self):
        self.log(
            "{}-{}: {}".format(
                NAME,
                VERSION,
                ", ".join(
                    [
                        "{} {}".format(
                            app.name,
                            app.icon,
                        )
                        for app in self.app_list
                    ]
                ),
            )
        )
        self.log(f"Type in Q.help() for help.")

    @property
    def l(self):
        return self.layer

    @property
    def p(self):
        return self.project

    def clear(self):
        # https://gis.stackexchange.com/a/216444/210095
        from qgis.PyQt.QtWidgets import QDockWidget

        consoleWidget = iface.mainWindow().findChild(QDockWidget, "PythonConsole")
        consoleWidget.console.shellOut.clearConsole()

        self.intro()

    def find_layer(self, layer_name):
        return QgsProject.instance().mapLayersByName(layer_name)

    def help(self):
        self.log("Q.clear()", "clear Python Console.")

        self.layer.help()
        if self.verbose:
            self.log("Q.list_of_layers()", "list of layers.")
            self.log("Q.load(filename,layer_name,template_name)", "load a layer.")
        self.project.help()

        if self.verbose:
            self.log("Q.refresh()", "refresh.")
            self.log("Q.reload()", "reload all layers.")
            self.log("Q.unload(layer_name)", "unload layer_name.")
        self.log("Q.verbose=True|False", "set verbose state.")

        for app in self.app_list:
            app.help()

    def list_of_layers(self, aux=False):
        output = [layer.name() for layer in QgsProject.instance().mapLayers().values()]
        if not aux:
            output = [
                layer_name
                for layer_name in output
                if not layer_name.startswith("Google")
                and not layer_name.startswith("template")
            ]
        self.log(
            "{} layer(s){}".format(
                len(output),
                ": {}".format(", ".join(output)) if self.verbose else "",
            ),
            icon="🔎",
        )
        return output

    def load(
        self,
        filename,
        layer_name,
        template_name="",
        refresh=True,
    ):
        if len(QGIS.find_layer(layer_name)) > 0:
            print(f"✅ {layer_name}")
            return True

        if filename.endswith(".geojson"):
            layer = QgsVectorLayer(filename, layer_name, "ogr")
        elif filename.endswith(".tif"):
            layer = QgsRasterLayer(filename, layer_name)
        else:
            self.log_error(f"cannot load {filename}.")
            return False

        if not layer.isValid():
            QGIS.show_error(f"invalid layer: {filename}.")
            return False

        QgsProject.instance().addMapLayer(layer)

        if template_name:
            template_layer = QGIS.find_layer(template_name)
            if not len(template_layer):
                QGIS.log_error(f"template not found: {template_name}.")
                return False

            # https://gis.stackexchange.com/a/357206/210095
            source_style = QgsMapLayerStyle()
            source_style.readFromLayer(template_layer[0])
            source_style.writeToLayer(layer)
            layer.triggerRepaint()

        self.log(layer_name, template_name, icon="🎨")

        if refresh:
            QGIS.refresh()

    def log(self, message, note="", icon="🌐"):
        print(
            "{} {}{}".format(
                icon,
                f"{message:.<40}" if note else message,
                note,
            )
        )

    def log_error(self, message, note=""):
        self.log(message, note, icon="❗️")

    def open_folder(self, path):
        if not path:
            self.log_error("path not found.")
            return

        self.log(path)
        os.system(f"open {path}")

    def refresh(self):
        iface.mapCanvas().refresh()

    def reload(self):
        # https://gis.stackexchange.com/a/449101/210095
        for layer in tqdm(QgsProject.instance().mapLayers().values()):
            layer.dataProvider().reloadData()

    def seed(self, command):
        hash_id = "{}-{:05d}".format(
            time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())),
            random.randrange(100000),
        )
        with open(
            os.path.join(
                abcli_QGIS_path_server,
                f"{hash_id}.command",
            ),
            "w",
        ) as f:
            f.write(command)

        self.log(hash_id, command, icon="🌱")

    def unload(self, layer_name, refresh=True):
        self.log(layer_name, icon="🗑️")

        for layer in self.find_layer(layer_name):
            QgsProject.instance().removeMapLayer(layer.id())

        if refresh:
            QGIS.refresh()


QGIS = ABCLI_QGIS()

Q = QGIS
layer = QGIS.layer
project = QGIS.project

vanwatch = ABCLI_QGIS_APPLICATION_VANWATCH()
QGIS.add_application(vanwatch)

QGIS.intro()
