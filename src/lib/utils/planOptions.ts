import L, { LatLng, Transformation, transformation } from "leaflet";
import kochi1Floor from '$lib/images/kochi1Floor.jpg'

const kochi1RefPoints = [410,1859] //y,x
const kochi1RefRatio = [3385/257.5,24425/1863]

const kochi1 = {
    crs: { 
        ...L.CRS.Simple, 
        transformation: new Transformation(kochi1RefRatio[1], kochi1RefPoints[1], -kochi1RefRatio[0], kochi1RefPoints[0]) 
    },
    image: kochi1Floor,
    width: 4963,
    height: 3509,
    minZoom: -100,
    zoom: -9,
    center: new LatLng(21647,8801),
    bounds: [
        new LatLng((0-kochi1RefPoints[0])*kochi1RefRatio[0],(0-kochi1RefPoints[1])*kochi1RefRatio[1]),
        new LatLng((3509-kochi1RefPoints[0])*kochi1RefRatio[0],(4963-kochi1RefPoints[1])*kochi1RefRatio[1])
    ]
}

export default kochi1;