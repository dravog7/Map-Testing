import type { TileLayerOptions } from "leaflet";


export interface ExtendedLayerOptions extends TileLayerOptions {
    [_: string]: unknown;
}
