/* eslint-disable @typescript-eslint/no-unused-vars */
import type { MapInfo } from '../interfaces/MapInfo';

const openStreet: MapInfo = {
    mapUrl: 'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
    option: {
        maxZoom: 19,
    }
}

const thunderforest: MapInfo = {
    mapUrl: 'https://tile.thunderforest.com/cycle/{z}/{x}/{y}.png?apikey={apikey}',
    option: {
        apikey: '1ee874a3fcba4022bb38b2407f40a677',
        maxZoom: 22
    }
}

const google: MapInfo = {
    mapUrl: 'http://{s}.google.com/vt?lyrs=m&x={x}&y={y}&z={z}',
    option: {
        maxZoom: 22,
        subdomains:['mt0','mt1','mt2','mt3']
    }
}


export default google