import sys
import lilv

PRESET_NS = 'http://lv2plug.in/ns/ext/presets'
RDFS_NS = 'http://www.w3.org/2000/01/rdf-schema'

world = lilv.World()
world.load_all()
preset_ns = lilv.Namespace(world, PRESET_NS)
rdfs_ns = lilv.Namespace(world, RDFS_NS)
plugins = world.get_all_plugins()

def get_presets(plugin_uri):
    plugin_uri = world.new_uri(plugin_uri)

    if plugin_uri is None or plugin_uri not in plugins:
        return "Plugin with URI '%s' not found" % plugin_uri

    plugin = plugins[plugin_uri]
    presets = plugin.get_related(getattr(preset_ns, '#Preset'))

    preset_map = {}

    for preset in presets:
        res = world.load_resource(preset)
        labels = world.find_nodes(preset, getattr(rdfs_ns, '#label'), None)

        if labels:
            label = str(labels[0])
        else:
            label = str(preset)
            print("Preset '&s' has no rdfs:label" % preset, file=sys.stderr)
        preset_map[label] = str(preset)
    return preset_map