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


def get_params(plugin_uri):
    plugin_uri = world.new_uri(plugin_uri)

    if plugin_uri is None or plugin_uri not in plugins:
        return "Plugin with URI '%s' not found" % plugin_uri

    params = []
    plugin = plugins[plugin_uri]
    for i in range(plugin.get_num_ports()):
        port = plugin.get_port_by_index(i)
        label = port.get_name()
        symbol = port.get_symbol()
        types = [str(t).rsplit("#", 1)[-1][:-4] for t in port.get_value(world.ns.rdf.type)]
        if('Control' in types):
            param = {
                "symbol": str(symbol),
                "label": str(label),
                "types": types,
            }
            xdefault, xminimum, xmaximum = port.get_range()
            if( xdefault is not None):                
                param['default'] = int(xdefault) if xdefault.is_int() else float(xdefault)
            if( xminimum is not None):                
                param['minimum'] = int(xminimum) if xminimum.is_int() else float(xminimum)
            if( xmaximum is not None):                
                param['maximum'] = int(xmaximum) if xmaximum.is_int() else float(xmaximum)
            params.append(param)
    return params
