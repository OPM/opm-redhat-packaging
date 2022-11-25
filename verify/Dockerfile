ARG version=""
ARG version_tag=""
FROM centos:7 AS stage1
ARG version
ARG version_tag
WORKDIR /tmp/opm
ADD . .
RUN echo "Configuring runtime environment"
RUN /bin/bash /tmp/opm/scripts/setup_runtime_env.sh
RUN useradd builder
RUN chown -R builder /tmp/opm/
USER builder
RUN echo "Cloning opm-tests"
RUN git clone --depth 1 https://github.com/OPM/opm-tests
USER root
FROM stage1 AS simulators_stage
RUN /bin/bash /tmp/opm/scripts/setup_simulators_env.sh
RUN echo "Running Norne checks"
USER builder
RUN /bin/bash /tmp/opm/scripts/run_norne.sh
USER root
FROM stage1 AS upscaling_stage
RUN /bin/bash /tmp/opm/scripts/setup_upscaling_env.sh
USER builder
RUN echo "Running upscaling checks"
RUN /bin/bash /tmp/opm/scripts/upscale_spe9.sh
