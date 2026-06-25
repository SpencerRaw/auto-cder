# cd-application

## Carbon Dot Application Validation

Designs and executes application validation experiments for synthesized carbon dots. Covers sensing, bioimaging, catalysis, and optoelectronic applications.

### Application Domains

| Domain | Key Metrics | Validation Protocol |
|---|---|---|
| **Metal Ion Sensing** | LOD, linear range, selectivity | Fluorescence quenching/turn-on titration, interference study (15+ ions) |
| **Bioimaging** | Cellular uptake, cytotoxicity, photostability | MTT assay, confocal imaging, bleaching comparison |
| **Photocatalysis** | Degradation rate, recyclability, ROS identification | Dye degradation kinetics, scavenger experiments, cycle tests |
| **Optoelectronics** | PLQY in film, carrier mobility, device stability | Film fabrication, I-V measurement, lifetime testing |
| **Antibacterial** | MIC, ROS generation, membrane integrity | Colony counting, DCFH-DA assay, SEM of treated bacteria |

### Stages

1. **Application Selection** — Match CD properties (emission, surface groups, size) to optimal application
2. **Protocol Design** — Design experiment with controls, replicates, and calibration standards
3. **Execution** — Run application validation experiments (wet-lab or simulation)
4. **Data Analysis** — Calculate performance metrics with error bars and statistical tests
5. **Benchmark Comparison** — Compare against literature CD systems for the same application

### Integration

- Reads characterization results from `cd-characterization`
- Reads application strategies from `cd-memory`
- Feeds application performance into `cd-memory` for strategy evolution

### Output Format

```yaml
application_report:
  domain: <sensing/bioimaging/catalysis/optoelectronics>
  analyte: <target molecule/ion/cell type>
  performance:
    detection_limit: <value> <unit>
    linear_range: [<min>, <max>] <unit>
    selectivity: <list of tested interferents with response>
    response_time: <seconds or minutes>
  comparison:
    benchmark_system: <literature reference>
    relative_performance: <better/comparable/worse>
    distinguishing_feature: <what makes this CD system unique>
```
