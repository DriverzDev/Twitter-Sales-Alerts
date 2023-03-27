import DriverzNFT from 0xa039bd7d55a96c0c
import MetadataViews from 0x1d7e57aa55817448

pub fun main(): MetadataViews.ExternalURL {
    return DriverzNFT.externalURL()
}